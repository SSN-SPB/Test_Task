from behave import when, given, then

from pytest_bdd_behave.pytest_bdd_behave03_arithmetic.arithmetic_functions import (
    add_integer,
)


@given("the first number is {a:d}")
def step_given_first_number(contex, a):
    contex.a = a


@when("add second number {b:d}")
def step_when_add_number(contex, b):
    contex.b = b
    contex.result = add_integer(contex.a, contex.b)


@then("the result sum is {expected:d}")
def step_then_result_sum(contex, expected):
    assert contex.result == expected
