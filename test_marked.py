import pytest

@pytest.mark.great
def test_isgreater():
    num = 100
    assert num > 90

@pytest.mark.less
def test_isless():
    num = 50
    assert num < 100