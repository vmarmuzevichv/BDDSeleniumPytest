Feature: Login actions
  User should be able login to the Nexportal


  Scenario: Successful login
    Given User on the Nexport login page
    When User uses correct credentials
    Then User should see home page
