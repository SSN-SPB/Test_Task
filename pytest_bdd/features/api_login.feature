Feature: API Login

  Scenario: Check pair usdrub is available
    Given the API is available
    When the response contains the expected fields
    Then the code is more than 100