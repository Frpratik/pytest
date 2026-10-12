import pytest

@pytest.mark.parametrize("num,output",[(1,11),(2,22),(3,34),(4,44)])
def test_ismultipleof(num,output):
    assert num * 11 == output