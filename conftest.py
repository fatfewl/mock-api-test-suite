import pytest
from utils.read_test_data import split_yaml_into_tests, get_test_ids

'''
We want to have pytest assert introspection in the helper function 
so we can see which assert failed and  the expected value
'''
pytest.register_assert_rewrite('call_endpoint')
pytest.register_assert_rewrite('tests')


def pytest_generate_tests(metafunc: object):
    """
    listener for every test. We ues this to parametrize the tests with data. The test data file must use the same
    name as the test function

    THIS IS CALLED BEFORE EVERY TEST FUNCTION
    """
    test_name = metafunc.definition.name
    test_data = split_yaml_into_tests(test_name)
    ids = get_test_ids(test_name)
    metafunc.parametrize("test_data", test_data, ids=ids)
