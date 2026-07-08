Feature: Multiply two numbers
  As a calculator user
  I want to multiply two numbers
  So that I can get the product

  Scenario: Multiply two positive numbers
    Given I have entered 5 into the calculator
    And I have entered 3 into the calculator
    When I press multiply
    Then the result should be 15

  Scenario: Multiply negative and positive numbers
    Given I have entered -4 into the calculator
    And I have entered 6 into the calculator
    When I press multiply
    Then the result should be -24

  Scenario: Multiply by zero
    Given I have entered 7 into the calculator
    And I have entered 0 into the calculator
    When I press multiply
    Then the result should be 0
