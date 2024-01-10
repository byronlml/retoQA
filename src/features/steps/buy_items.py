from behave import *
from src.pages.buy_items.buy_items import BuyItemsPage
from src.pages.login.login import LoginPage


@Given('Enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    LoginPage(context.driver).login_user(username, password)


@Given('I click on add card button')
def card(context):
    BuyItemsPage(context.driver).add_card_1()
    BuyItemsPage(context.driver).add_card_2()


@when('I click on shopping cart icon')
def shopping(context):
    BuyItemsPage(context.driver).shipping()


@when('I click on checkout')
def checkout(context):
    BuyItemsPage(context.driver).checkout()


@when('I complete the form "{first_name}", "{last_name}" and "{postal_code}"')
def form(context, first_name, last_name, postal_code):
    BuyItemsPage(context.driver).first_name(first_name)
    BuyItemsPage(context.driver).last_name(last_name)
    BuyItemsPage(context.driver).postal_code(postal_code)


@when('I click on the continue button')
def continue_button(context):
    BuyItemsPage(context.driver).click_continue()


@when('I click on the finish button')
def finish(context):
    BuyItemsPage(context.driver).finish()


@when('should show the message thank you for your purchase')
def purchase(context):
    text = BuyItemsPage(context.driver).verify_buy()
    assert text == "Thank you for your order!"


@when('I click on the menu button')
def menu(context):
    BuyItemsPage(context.driver).menu()


@then('I click on logout button')
def logout(context):
    BuyItemsPage(context.driver).logout()
