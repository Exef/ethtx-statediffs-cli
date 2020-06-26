import json

def transform(storage_layout):
    return []


if __name__ == "__main__":
    from pprint import pp

    with open("dssStorageLayout.json") as storage_layout_json:
        storage_layout = json.load(storage_layout_json)
        ethtx_storage_description = transform(storage_layout)

        pp(ethtx_storage_description)
