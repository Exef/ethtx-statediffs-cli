import json
import re
import pprint
from itertools import tee, islice, zip_longest


pp = pprint.PrettyPrinter(indent=4)


def get_next(some_iterable, window=1):
    items, nexts = tee(some_iterable, 2)
    nexts = islice(nexts, window, None)
    return zip_longest(items, nexts)


def get_storage_layout(storage_layout_from_compiler):
    for _, data_by_contract_file_name in storage_layout_from_compiler.get("contracts", storage_layout_from_compiler).items():
        for _, data_by_contract_name in data_by_contract_file_name.items():
            return data_by_contract_name["storageLayout"]


def get_type(layout_type):
    if layout_type == None:
        return None
    if re.search("mapping", layout_type):
        return "hashmap"
    if re.search("int", layout_type):
        return "int"
    if re.search("address", layout_type):
        return "address"
    if re.search("bytes", layout_type):
        return "string"
    if re.search("struct", layout_type):
        return "struct"


def parse_hashmap_key_value(value_description):
    key2_description = value_description[value_description.find(
        "(")+1:value_description.find(",")]
    value2_description = value_description[value_description.find(
        ",")+1:value_description.rfind(")")]
    key2 = get_type(key2_description)
    value2 = get_type(value2_description)
    return key2, key2_description, value2, value2_description


def parse_struct_values(type_description, type_layouts):
    struct_description = type_layouts[type_description]
    members = struct_description.get("members")
    members = [{"name": member.get("label"), "shift": int(member.get("slot")), "type": get_type(member.get("type"))}
               for member in members]
    return members


def build_hashmap_description(type, type_layouts):
    type_description = type_layouts[type]
    key1_description = type_description.get("key")
    value1_description = type_description.get("value")

    struct = None
    key2 = None
    value2 = None

    value1 = get_type(value1_description)
    key1 = get_type(key1_description)
    pp.pprint("key1: %s key1 description: %s" % (key1, key1_description))

    if value1 == "struct":
        struct = parse_struct_values(value1_description, type_layouts)
    elif value1 == "hashmap":
        key2, _, value2, value2_description = parse_hashmap_key_value(
            value1_description)
        key1, key2 = key2, key1
        if value2 == "struct":
            struct = parse_struct_values(value2_description, type_layouts)
        if value2 == "hashmap":
            # too many keys
            pp.pprint("too many keys")

    pp.pprint("value1: %s value2 %s key1: %s key2: %s" %
              (value1, value2, key1, key2))

    return {
        "key1": key1,
        "key2": key2,
        "struct": struct,
        "value": value2 if value2 != None else value1
    }


def get_slot_end(next_layout):
    if next_layout == None:
        return 63
    next_offset = int(next_layout["offset"])
    if next_offset == None:
        return 63
    if next_offset == 0:
        return 63
    return next_offset - 1


def transform(storage_layout_from_compiler):
    storage_layout = get_storage_layout(storage_layout_from_compiler)
    transformed = []
    for layout, next_layout in get_next(storage_layout["storage"]):
        current_type = get_type(layout["type"])
        description = {
            "name": layout["label"],
            "slot": int(layout["slot"]),
            "start": int(layout["offset"]),
            "end": get_slot_end(next_layout),
            "type": current_type,
        }

        if current_type == "hashmap":
            description["hashmap"] = build_hashmap_description(
                layout["type"],
                storage_layout["types"]
            )
        else:
            description["hashmap"] = None

        transformed.append(description)

    return transformed


if __name__ == "__main__":
    with open("dssStorageLayout.json") as storage_layout_json:
        storage_layout = json.load(storage_layout_json)
        ethtx_storage_description = transform(storage_layout)

        pp.pprint(ethtx_storage_description)
