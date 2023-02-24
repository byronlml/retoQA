Feature: Perform login
  @LoginOk
   Scenario: Login
     When I open the saucedemo page
     And Enter username "standard_user" and password "secret_sauce"
     Then Click on login button



  @LoginSmoke
   Scenario Outline: Login with multiple parameters
     When I open the saucedemo page
     And Enter username "<username>" and password "<password>"
     Then Click on login button

     Examples:
      | username | password |
      | standard_user  | 123      |
      | locked_out_user | 123      |