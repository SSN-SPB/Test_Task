Feature: Login

  Scenario: Successful login
    Given I am on the login page
    When I log in with username "Admin" and password "Pass123!"
    Then I should see the data page