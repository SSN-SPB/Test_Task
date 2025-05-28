#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize("used, expected", [(1, 0), (2, 1), (3, 2)])
def test_minus_one(used, expected):
    assert used - 1 == expected


@pytest.mark.parametrize("used, expected", [([1, 1], 2), ([1, 8], 9), ([1, -1], 0)])
def test_sum(used, expected):
    assert used[0] + used[1] == expected
