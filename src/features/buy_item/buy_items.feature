Feature: Perform Buy Item

  Background: User is logged
     Given I open the saucedemo page
     And Enter username "standard_user" and password "secret_sauce"
     Then Click on login button

   Scenario: Buy Item
     Given I click on add card button
     When I click on shopping cart icon
     And I click on checkout
     And I complete the form "<name>", "<lastName>" and "<postalCode>"
     And I click on the continue button
     And I click on the finish button
     And should show the message thank you for your purchase
     And I click on the menu button
     Then I click on logout button

