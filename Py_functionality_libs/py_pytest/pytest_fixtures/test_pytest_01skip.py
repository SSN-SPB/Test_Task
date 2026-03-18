import pytest

@pytest.mark.skip(reason="Not implemented yet")
def test_skipped():
    assert False

@pytest.mark.not_skipped
def test_not_skipped():
    assert 1 == 1
