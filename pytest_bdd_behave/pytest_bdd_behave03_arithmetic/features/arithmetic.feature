Feature: As a User
    I want to get sum of two values
    So I could use this value in future

Scenario: Add positive number
    Given the first number is 5
    When add second number 3
    Then the result sum is 8

Scenario: Add negative number
    Given the first number is 5
    When add second number -3
    Then the result sum is 2

Scenario: Add zero value
    Given the first number is 5
    When add second number 0
    Then the result sum is 5
