import pytest


@pytest.fixture
def setup():
    print("setup")


@pytest.mark.usefixtures("setup")
def test_something():
    assert True
