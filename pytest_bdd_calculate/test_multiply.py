import pytest
from pytest_bdd import scenarios, given, when, then

from calculator import Calculator

# Load all scenarios from the feature file
scenarios("features/multiply.feature")


@pytest.fixture
def calculator():
    """Provide a calculator instance for each test."""
    return Calculator()


@given("I have entered 5 into the calculator", target_fixture="calculator")
def enter_5(calculator):
    calculator.enter(5)
    return calculator


@given("I have entered 3 into the calculator", target_fixture="calculator")
def enter_3(calculator):
    calculator.enter(3)
    return calculator


@given("I have entered -4 into the calculator", target_fixture="calculator")
def enter_minus_4(calculator):
    calculator.enter(-4)
    return calculator


@given("I have entered 6 into the calculator", target_fixture="calculator")
def enter_6(calculator):
    calculator.enter(6)
    return calculator


@given("I have entered 7 into the calculator", target_fixture="calculator")
def enter_7(calculator):
    calculator.enter(7)
    return calculator


@given("I have entered 0 into the calculator", target_fixture="calculator")
def enter_0(calculator):
    calculator.enter(0)
    return calculator


@when("I press multiply")
def press_multiply(calculator):
    calculator.multiply()


@then("the result should be 15")
def check_15(calculator):
    assert calculator.get_result() == 15


@then("the result should be -24")
def check_minus_24(calculator):
    assert calculator.get_result() == -24


@then("the result should be 0")
def check_0(calculator):
    assert calculator.get_result() == 0
