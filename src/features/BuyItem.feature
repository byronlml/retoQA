Feature: Perform Buy Item

   Scenario: Buy Item
     When I open the saucedemo page
     And Enter username "standard_user" and password "secret_sauce"
     And Click on login button
     And I click on add card button
     And I click on shopping cart icon
     And I click on checkout
     And I complete the form
     And I click on the continue button
     And I click on the finish button
     Then should show the message thank you for your purchase


  @LoginSmoke
   Scenario Outline: Login with multiple parameters
     When I open the saucedemo page
     And Enter username "<username>" and password "<password>"
     Then Click on login button

     Examples:
      | username | password |
      | standard_user  | 123      |
      | locked_out_user | 123      |