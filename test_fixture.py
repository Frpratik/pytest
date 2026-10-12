import pytest

"""
we cant access this fixture outside this file ,
if then we have to create file named "conftest.py"
then it will be accesseble to all files

"""
@pytest.fixture
def input_value():
    input = 40
    return input

def test_isdivisibleby4(input_value):
    assert input_value % 4 == 0


def test_isdivisibleby3(input_value):
    assert input_value % 3 == 0