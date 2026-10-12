import pytest

#this test will get skipped 
@pytest.mark.skip
def test_addition():
    num1 = 5
    num2 = 6
    assert num1 + num2 == 10

#only this test will run
def test_subtraction():
    num1 = 5
    num2 = 6
    assert num1 - num2 == -1
