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
    assert(
        test_storage_layout) == test_contract_input_data["test.sol"]["Test"]["storageLayout"]


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


def test_reads_vat_can_correctly():
    variable_descriptions = transform(input_data)

    can = variable_descriptions[1]
    assert can["name"] == expected_output_data[1]["name"]
    assert can["slot"] == expected_output_data[1]["slot"]
    assert can["start"] == expected_output_data[1]["start"]
    assert can["type"] == expected_output_data[1]["type"]
    assert can["hashmap"] == expected_output_data[1]["hashmap"]

    # assert can == expected_output_data[1]


def test_reads_vat_ilks_correctly():
    variable_descriptions = transform(input_data)

    ilks = variable_descriptions[2]
    assert ilks["name"] == expected_output_data[2]["name"]
    assert ilks["slot"] == expected_output_data[2]["slot"]
    assert ilks["start"] == expected_output_data[2]["start"]
    assert ilks["type"] == expected_output_data[2]["type"]
    assert ilks["hashmap"] == expected_output_data[2]["hashmap"]

    # assert ilks == expected_output_data[2]

# assert ilks["end"] == expected_output_data[2]["end"]
# assert can["hashmap"] == expected_output_data[1]["hashmap"]


def test_reads_vat_urns_correctly():
    variable_descriptions = transform(input_data)

    urns = variable_descriptions[3]
    assert urns["name"] == expected_output_data[3]["name"]
    assert urns["slot"] == expected_output_data[3]["slot"]
    assert urns["start"] == expected_output_data[3]["start"]
    assert urns["type"] == expected_output_data[3]["type"]
    assert urns["hashmap"] == expected_output_data[3]["hashmap"]

    # assert urns == expected_output_data[3]


def test_reads_vat_gem_correctly():
    variable_descriptions = transform(input_data)

    gem = variable_descriptions[4]
    assert gem["name"] == expected_output_data[4]["name"]
    assert gem["slot"] == expected_output_data[4]["slot"]
    assert gem["start"] == expected_output_data[4]["start"]
    assert gem["type"] == expected_output_data[4]["type"]
    assert gem["hashmap"] == expected_output_data[4]["hashmap"]

    # assert gem == expected_output_data[4]


def test_reads_vat_dai_correctly():
    variable_descriptions = transform(input_data)

    dai = variable_descriptions[5]
    assert dai["name"] == expected_output_data[5]["name"]
    assert dai["slot"] == expected_output_data[5]["slot"]
    assert dai["start"] == expected_output_data[5]["start"]
    assert dai["type"] == expected_output_data[5]["type"]
    assert dai["hashmap"] == expected_output_data[5]["hashmap"]

    # assert dai == expected_output_data[5]


def test_reads_vat_sin_correctly():
    variable_descriptions = transform(input_data)

    sin = variable_descriptions[6]
    assert sin["name"] == expected_output_data[6]["name"]
    assert sin["slot"] == expected_output_data[6]["slot"]
    assert sin["start"] == expected_output_data[6]["start"]
    assert sin["type"] == expected_output_data[6]["type"]
    assert sin["hashmap"] == expected_output_data[6]["hashmap"]

    # assert sin == expected_output_data[6]


def test_reads_vat_debt_correctly():
    variable_descriptions = transform(input_data)

    debt = variable_descriptions[7]
    assert debt["name"] == expected_output_data[7]["name"]
    assert debt["slot"] == expected_output_data[7]["slot"]
    assert debt["start"] == expected_output_data[7]["start"]
    assert debt["type"] == expected_output_data[7]["type"]
    assert debt["hashmap"] == expected_output_data[7]["hashmap"]

    # assert debt == expected_output_data[7]


def test_reads_vat_vice_correctly():
    variable_descriptions = transform(input_data)

    vice = variable_descriptions[8]
    assert vice["name"] == expected_output_data[8]["name"]
    assert vice["slot"] == expected_output_data[8]["slot"]
    assert vice["start"] == expected_output_data[8]["start"]
    assert vice["type"] == expected_output_data[8]["type"]
    assert vice["hashmap"] == expected_output_data[8]["hashmap"]

    # assert vice == expected_output_data[8]


def test_reads_vat_Line_correctly():
    variable_descriptions = transform(input_data)

    line = variable_descriptions[9]
    assert line["name"] == expected_output_data[9]["name"]
    assert line["slot"] == expected_output_data[9]["slot"]
    assert line["start"] == expected_output_data[9]["start"]
    assert line["type"] == expected_output_data[9]["type"]
    assert line["hashmap"] == expected_output_data[9]["hashmap"]

    # assert line == expected_output_data[9]


def test_reads_vat_live_correctly():
    variable_descriptions = transform(input_data)

    live = variable_descriptions[10]
    assert live["name"] == expected_output_data[10]["name"]
    assert live["slot"] == expected_output_data[10]["slot"]
    assert live["start"] == expected_output_data[10]["start"]
    assert live["type"] == expected_output_data[10]["type"]
    assert live["hashmap"] == expected_output_data[10]["hashmap"]

    # assert live == expected_output_data[8]
