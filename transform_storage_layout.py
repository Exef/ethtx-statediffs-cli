import json
import re

def get_storage_layout(storage_layout_from_compiler):
    for _, data_by_contract_file_name in storage_layout_from_compiler.items():
        for _, data_by_contract_name in  data_by_contract_file_name.items():
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

def build_type_description(types_layout, type):
    type_description = types_layout[type]
    key1 = get_type(type_description.get("key", None))
    value = get_type(type_description.get("value", None))

    return {
        "key1": key1,
        "key2": None,
        "struct": None,
        "value": value
    }

def transform(storage_layout_from_compiler):
    storage_layout = get_storage_layout(storage_layout_from_compiler)
    transformed = []
    for layout in storage_layout["storage"]:
        current_type = get_type(layout["type"])
        description = {
            "name": layout["label"],
            "slot": int(layout["slot"]),
            "start": layout["offset"],
            "type": current_type,
            current_type: build_type_description(
                storage_layout["types"],
                layout["type"]
            )
        }

        transformed.append(description)

    return transformed

if __name__ == "__main__":
    from pprint import pp

    with open("dssStorageLayout.json") as storage_layout_json:
        storage_layout = json.load(storage_layout_json)
        ethtx_storage_description = transform(storage_layout)

        pp(ethtx_storage_description)
