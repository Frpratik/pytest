import pytest

#this test will not print reason of failure or error in detail.
@pytest.mark.xfail
def test_addition():
    num1 = 5
    num2 = 6
    assert num1 + num2 == 10

#this test will print reason of failure or error in detail.
def test_subtraction():
    num1 = 5
    num2 = 6
    assert num1 - num2 == 0

    