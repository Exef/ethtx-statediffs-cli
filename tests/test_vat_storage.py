import pytest
import json

from transform_storage_layout import transform

input_data = {}
with open("./tests/inputs/vatStorageLayout.json") as input_data_json:
    input_data = json.load(input_data_json)

expected_output_data = {}
with open("./tests/outputs/vatStorageDescription.json") as expected_output_json:
    expected_output_data = json.load(expected_output_json)

def test_transforms_vat_contract_storage_description():
    variable_descriptions = transform(input_data)

    assert len(variable_descriptions) == len(expected_output_data)

    for index, expected_var_description in enumerate(expected_output_data):
        assert expected_var_description == variable_descriptions[index]

def test_reads_vat_wards_correctly():
    variable_descriptions = transform(input_data)

    wards = variable_descriptions[0]
    assert wards == expected_output_data[0]


def test_reads_vat_can_correctly():
    variable_descriptions = transform(input_data)

    can = variable_descriptions[1]
    assert can == expected_output_data[1]


def test_reads_vat_ilks_correctly():
    variable_descriptions = transform(input_data)

    ilks = variable_descriptions[2]
    assert ilks == expected_output_data[2]


def test_reads_vat_urns_correctly():
    variable_descriptions = transform(input_data)

    urns = variable_descriptions[3]
    assert urns == expected_output_data[3]


def test_reads_vat_gem_correctly():
    variable_descriptions = transform(input_data)

    gem = variable_descriptions[4]
    assert gem == expected_output_data[4]


def test_reads_vat_dai_correctly():
    variable_descriptions = transform(input_data)

    dai = variable_descriptions[5]
    assert dai == expected_output_data[5]

def test_reads_vat_sin_correctly():
    variable_descriptions = transform(input_data)

    sin = variable_descriptions[6]
    assert sin == expected_output_data[6]


def test_reads_vat_debt_correctly():
    variable_descriptions = transform(input_data)

    debt = variable_descriptions[7]
    assert debt == expected_output_data[7]


def test_reads_vat_vice_correctly():
    variable_descriptions = transform(input_data)

    vice = variable_descriptions[8]
    assert vice == expected_output_data[8]


def test_reads_vat_Line_correctly():
    variable_descriptions = transform(input_data)

    line = variable_descriptions[8]
    assert line == expected_output_data[8]


def test_reads_vat_live_correctly():
    variable_descriptions = transform(input_data)

    live = variable_descriptions[8]
    assert live == expected_output_data[8]