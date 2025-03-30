import pytest


def counting(value):
    result = value + 1
    return result


@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
def test_check_pytest_assert_parameterized(n, expected):
    assert counting(n) == expected
