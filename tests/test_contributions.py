import pytest
from utils.call_endpoint import post_to_endpoint
from utils.read_test_data import json_schema_loader
from jsonschema import validate


@pytest.mark.sanity
def test_get_contribution_valid(test_data):
    contribution_api_test(test_data)


def test_get_contribution_invalid(test_data):
    contribution_api_test(test_data)


def test_set_contribution_valid(test_data):
    contribution_api_test(test_data)


def test_set_contribution_invalid(test_data):
    contribution_api_test(test_data)


def contribution_api_test(test_data):
    resp = post_to_endpoint(test_data['method'], test_data['headers'], test_data)
    assert resp.status_code == test_data['expected-status-code']
    assert resp.json() == test_data['expected-response']
    validate(resp.json(), json_schema_loader(test_data['schema']))
