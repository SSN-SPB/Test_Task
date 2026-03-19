import pytest


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 2, 3),
        (2, 3, 5),
    ],
)
def test_add(x, y, expected):
    assert x + y == expected
