import json
import yaml
import os

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), '../resources/test-data/')
JSON_SCHEMA_DIR = os.path.join(os.path.dirname(__file__), '../resources/schemas/')


def _read_test_data_yaml(file_name):
    """Read a yaml file containing test data into mem as one block
    """
    filepath = os.path.join(TEST_DATA_DIR, file_name + '.yaml')
    with open(filepath, "r", encoding="utf-8") as fil_descriptor:
        data = yaml.safe_load(fil_descriptor)
    return data


def split_yaml_into_tests(data_file):
    """Split yaml block (file) into tests and put each test into a tuple
        so as to be ready for pytest.
    """

    # now read in the test data file
    test_data = _read_test_data_yaml(data_file)
    # finally, split the yaml by test case ready for pytest
    split_test_data = []
    for tc_id, tst in test_data.items():
        split_test_data.append(test_data[tc_id])

    return tuple(split_test_data)


def get_test_ids(data_file):
    """Get just the test ids and description of each test
        and ignore the test data. Used for pytest parameterization.
    """
    data = _read_test_data_yaml(data_file)
    keys = []
    for key in data.keys():
        keys.append(key)
    return keys


def json_schema_loader(filepath):
    """Read json file as json object.
    """
    filepath = JSON_SCHEMA_DIR + filepath + ".json"
    with open(filepath, "r") as fil_descriptor:
        data = json.load(fil_descriptor)
        return data
