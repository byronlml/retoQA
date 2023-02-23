Feature: Perform Logout
  Scenario: Logout
     When I open the saucedemo page
     And Enter username "standard_user" and password "secret_sauce"
     And Click on login button
     And I click on the menu button
     And I click on logout button
     Then should show the page login