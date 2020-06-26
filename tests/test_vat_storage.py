import pytest
import json

from transform_storage_layout import get_storage_layout, transform

input_data = {}
with open("./tests/inputs/vatStorageLayout.json") as input_data_json:
    input_data = json.load(input_data_json)

expected_output_data = {}
with open("./tests/outputs/vatStorageDescription.json") as expected_output_json:
    expected_output_data = json.load(expected_output_json)

test_contract_input_data = {
    "test.sol": {
        "Test": {
            "storageLayout": {
                "storage": [
                    {
                        "astId": 6537,
                        "contract": "vat.sol:Vat",
                        "label": "live",
                        "offset": 0,
                        "slot": "10",
                        "type": "t_uint256"
                    }
                ],
                "types": {
                    "t_address": {
                        "encoding": "inplace",
                        "label": "address",
                        "numberOfBytes": "20"
                    },
                    "t_uint256": {
                        "encoding": "inplace",
                        "label": "uint256",
                        "numberOfBytes": "32"
                    }
                }
            }
        }
    }
}

def test_gets_storage_layout_from_compiled_layout():
    vat_storage_layout = get_storage_layout(input_data)
    test_storage_layout = get_storage_layout(test_contract_input_data)

    assert(vat_storage_layout) == input_data["vat.sol"]["Vat"]["storageLayout"]
    assert(test_storage_layout) == test_contract_input_data["test.sol"]["Test"]["storageLayout"]

def test_transforms_vat_contract_storage_description():
    variable_descriptions = transform(input_data)

    assert len(variable_descriptions) == len(expected_output_data)

def test_reads_vat_wards_correctly():
    variable_descriptions = transform(input_data)

    wards = variable_descriptions[0]
    assert wards["name"] == expected_output_data[0]["name"]
    assert wards["slot"] == expected_output_data[0]["slot"]
    assert wards["start"] == expected_output_data[0]["start"]
    assert wards["type"] == expected_output_data[0]["type"]
    assert wards["hashmap"] == expected_output_data[0]["hashmap"]

    # assert wards == expected_output_data[0]


# def test_reads_vat_can_correctly():
#     variable_descriptions = transform(input_data)

#     can = variable_descriptions[1]
#     assert can == expected_output_data[1]


# def test_reads_vat_ilks_correctly():
#     variable_descriptions = transform(input_data)

#     ilks = variable_descriptions[2]
#     assert ilks == expected_output_data[2]


# def test_reads_vat_urns_correctly():
#     variable_descriptions = transform(input_data)

#     urns = variable_descriptions[3]
#     assert urns == expected_output_data[3]


# def test_reads_vat_gem_correctly():
#     variable_descriptions = transform(input_data)

#     gem = variable_descriptions[4]
#     assert gem == expected_output_data[4]


# def test_reads_vat_dai_correctly():
#     variable_descriptions = transform(input_data)

#     dai = variable_descriptions[5]
#     assert dai == expected_output_data[5]

# def test_reads_vat_sin_correctly():
#     variable_descriptions = transform(input_data)

#     sin = variable_descriptions[6]
#     assert sin == expected_output_data[6]


# def test_reads_vat_debt_correctly():
#     variable_descriptions = transform(input_data)

#     debt = variable_descriptions[7]
#     assert debt == expected_output_data[7]


# def test_reads_vat_vice_correctly():
#     variable_descriptions = transform(input_data)

#     vice = variable_descriptions[8]
#     assert vice == expected_output_data[8]


# def test_reads_vat_Line_correctly():
#     variable_descriptions = transform(input_data)

#     line = variable_descriptions[8]
#     assert line == expected_output_data[8]


# def test_reads_vat_live_correctly():
#     variable_descriptions = transform(input_data)

#     live = variable_descriptions[8]
#     assert live == expected_output_data[8]
