Feature: Login functionality

  Scenario: Successful login
    Given the username is "admin"
    When the password is "1234"
    Then login should be successful