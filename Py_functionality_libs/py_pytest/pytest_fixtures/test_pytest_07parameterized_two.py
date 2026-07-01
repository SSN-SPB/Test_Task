import pytest

num_list = [1, 2, 3]


@pytest.fixture(params=num_list)
def num(request):
    return request.param


def test_param(num):
    assert num in num_list
