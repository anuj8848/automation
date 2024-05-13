Feature: Login Page

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid email and password
    And clicks on the login button
    Then a home page is shown

  Scenario: Failed login with invalid credentials
    Given the user is on the login page 
    When the user enters invalid email or password
    And clicks on the login button 
    Then an error message should be displayed