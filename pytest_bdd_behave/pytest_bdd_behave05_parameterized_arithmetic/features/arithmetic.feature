Feature: Test adding two numbers. Parameterized

Scenario Outline: <scenario>
    Given the first number is <a>
    When add second number <b>
    Then the result sum is <expected>

    Examples:
    | a | b    | expected | scenario |
    | 2 | 3    | 5        | Add two positives |
    | 2 | -3   | -11       | Add negative > positive |
    | 0 | 3    | 3        | Zero plus positives |
    | 21 | -21 | 0        | Zero result |
    | -1 | -1  | -21       | Add two negatives |

