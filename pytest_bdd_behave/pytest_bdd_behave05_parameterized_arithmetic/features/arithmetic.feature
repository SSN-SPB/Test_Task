Feature: Test mathematic operations Parameterized

Scenario Outline: Adding - <scenario>
    Given the first number is <a>
    When add second number <b>
    Then the result sum is <expected>

    Examples:
    | a | b    | expected | scenario |
    | 2 | 3    | 5        | Add two positives |
    | 2 | -3   | -1       | Add negative > positive |
    | 0 | 3    | 3        | Zero plus positives |
    | 21 | -21 | 0        | Zero result |
    | -1 | -1  | -2       | Add two negatives |



Scenario Outline: Subtract - <scenario>
    Given the first number is <a>
    When I subtract the second number <b>
    Then the result subtract is <expected>

    Examples:
    | a | b    | expected  | scenario |
    | 2 | 3    | -1        | Subtract two positives |
    | 2 | -3   | 5         | Subtract negative > positive |
    | 0 | 3    | -3        | Zero plus positives |
    | 21 | -21 | 42        | Zero result |
    | -1 | -1  | 0         | Subtract two negatives |

