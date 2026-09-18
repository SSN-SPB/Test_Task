from behave import when, given, then

from pytest_bdd_behave.pytest_bdd_behave05_parameterized_arithmetic.arithmetic_functions import (
    subtract_integer,
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


@when("I subtract the second number {b:d}")
def step_when_subtrack_number(contex, b):
    contex.b = b
    contex.result = subtract_integer(contex.a, contex.b)


@then("the result subtract is {expected:d}")
def step_then_result_subtrack(contex, expected):
    assert contex.result == expected
