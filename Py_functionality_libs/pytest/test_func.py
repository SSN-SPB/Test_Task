# run by
# python -m pytest -v test_func.py

def test_calc_addition():
    """Verify the output of `calc_addition` function"""
    output = 2 + 4
    assert output == 6


def test_calc_substraction():
    """Verify the output of `calc_substraction` function"""
    output = 2 - 4
    assert output == -2


def test_calc_multiply():
    """Verify the output of `calc_multiply` function"""
    output = 2 * 4
    assert output == 8
