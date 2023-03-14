import time
from behave import *
from src.Pages.BuyItems import BuyItem
from src.Pages.Login import LoginPage


@Given('Enter username "{username}" and password "{password}"')
def step_impl(self, username, password):
    LoginPage(self.driver).username(username)
    LoginPage(self.driver).password(password)


@Given('I click on add card button')
def card(self):
    BuyItem(self.driver).add_card_1()
    time.sleep(2)
    BuyItem(self.driver).add_card_2()


@when('I click on shopping cart icon')
def shopping(self):
    BuyItem(self.driver).shipping()


@when('I click on checkout')
def checkout(self):
    BuyItem(self.driver).checkout()


@when('I complete the form "{first_name}", "{last_name}" and "{postal_code}"')
def form(self, first_name, last_name, postal_code):
    BuyItem(self.driver).first_name(first_name)
    BuyItem(self.driver).last_name(last_name)
    BuyItem(self.driver).postal_code(postal_code)


@when('I click on the continue button')
def continue_button(self):
    BuyItem(self.driver).click_continue()


@when('I click on the finish button')
def finish(self):
    BuyItem(self.driver).finish()


@when('should show the message thank you for your purchase')
def purchase(self):
    text = BuyItem(self.driver).verify_buy()
    assert text == "Thank you for your order!"


@when('I click on the menu button')
def menu(self):
    BuyItem(self.driver).menu()
    time.sleep(3)


@then('I click on logout button')
def logout(self):
    BuyItem(self.driver).logout()






