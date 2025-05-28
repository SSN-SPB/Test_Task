#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(params=[-11, 2, 3])
def get_parameter(request):
    return request.param


def test_if_parameter_positive(get_parameter):
    assert get_parameter > 1


if __name__ == "__main__":
    pytest.main()
