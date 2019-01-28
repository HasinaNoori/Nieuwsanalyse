"""
You can auto-discover and run all tests with this command:

    py.test

Documentation: https://docs.pytest.org/en/latest/
"""

from CoolPackageName import cool_file_name


def test_it_get_correct_string():
    assert(cool_file_name.get_string() == 'Hello world!')
