import json

def get_storage_layout(storage_layout_from_compiler):
    for _, data_by_contract_file_name in storage_layout_from_compiler.items():
        for _, data_by_contract_name in  data_by_contract_file_name.items():
            return data_by_contract_name["storageLayout"]


def transform(storage_layout_from_compiler):
    storage_layout = get_storage_layout(storage_layout_from_compiler)
    transformed = []
    for layout in storage_layout["storage"]:
        transformed.append(layout)

    return transformed


if __name__ == "__main__":
    from pprint import pp

    with open("dssStorageLayout.json") as storage_layout_json:
        storage_layout = json.load(storage_layout_json)
        ethtx_storage_description = transform(storage_layout)

        pp(ethtx_storage_description)



# {
#   "vat.sol": {
#     "Vat": {
#       "storageLayout": {
#         "storage": [
#           {
#             "astId": 6537,
#             "contract": "vat.sol:Vat",
#             "label": "live",
#             "offset": 0,
#             "slot": "10",
#             "type": "t_uint256"
#           }
#         ],
#         "types": {
#           "t_address": {
#             "encoding": "inplace",
#             "label": "address",
#             "numberOfBytes": "20"
#           },
#           "t_mapping(t_bytes32,t_struct(Ilk)6500_storage)": {
#             "encoding": "mapping",
#             "key": "t_bytes32",
#             "label": "mapping(bytes32 => struct Vat.Ilk)",
#             "numberOfBytes": "32",
#             "value": "t_struct(Ilk)6500_storage"
#           },
#           "t_struct(Ilk)6500_storage": {
#             "encoding": "inplace",
#             "label": "struct Vat.Ilk",
#             "members": [
#               {
#                 "astId": 6491,
#                 "contract": "vat.sol:Vat",
#                 "label": "Art",
#                 "offset": 0,
#                 "slot": "0",
#                 "type": "t_uint256"
#               },
#               {
#                 "astId": 6493,
#                 "contract": "vat.sol:Vat",
#                 "label": "rate",
#                 "offset": 0,
#                 "slot": "1",
#                 "type": "t_uint256"
#               },
#               {
#                 "astId": 6495,
#                 "contract": "vat.sol:Vat",
#                 "label": "spot",
#                 "offset": 0,
#                 "slot": "2",
#                 "type": "t_uint256"
#               },
#             ],
#             "numberOfBytes": "160"
#           },
#           "t_struct(Urn)6505_storage": {
#             "encoding": "inplace",
#             "label": "struct Vat.Urn",
#             "members": [
#               {
#                 "astId": 6502,
#                 "contract": "vat.sol:Vat",
#                 "label": "ink",
#                 "offset": 0,
#                 "slot": "0",
#                 "type": "t_uint256"
#               },
#               {
#                 "astId": 6504,
#                 "contract": "vat.sol:Vat",
#                 "label": "art",
#                 "offset": 0,
#                 "slot": "1",
#                 "type": "t_uint256"
#               }
#             ],
#             "numberOfBytes": "64"
#           },
#           "t_uint256": {
#             "encoding": "inplace",
#             "label": "uint256",
#             "numberOfBytes": "32"
#           }
#         }
#       }
#     }
#   }
# }