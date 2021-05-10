Feature: Authentication

  Scenario: Login page opened and no credentials were provided
    Given we are on the login page
    Then the email field has no error class

  Scenario Outline: Login email is invalid
    Given we are on the login page
    Given an email as "<email>"
    When we set the email
    Then the email field gets an error class

    Examples: Emails
      | email           |
      |                 |
      | invalid email   |

  Scenario Outline: Login email is valid
    Given we are on the login page
    Given an email as "<email>"
    When we set the email
    Then the email field gets an ok class

    Examples: Emails
      | email           |
      | test@test.com   |

  Scenario Outline: Invalid credentials
    Given we are on the login page
    Given an email as "<email>"
    Given a password as "<password>"
    Given an error message as "<error_message>"
    When we set the credentials
    And click the Login button
    Then the expected error message is shown

    Examples: Credentials and errors
      | email           | password         | error_message              |
      |                 |                  | An email address required. |
      |                 | invalid password | An email address required. |
      | invalid email   |                  | Invalid email address.     |
      | test@user.com   |                  | Password is required.      |
      | test@user.com   | invalid password | Authentication failed.     |