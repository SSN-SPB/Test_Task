import pytest

num_list = [1, 2, 3]


@pytest.fixture(autouse=True)
def auto():
    print("runs for every test")


@pytest.fixture(params=num_list)
def num(request):
    return request.param


def test_param(num):
    assert num in num_list
