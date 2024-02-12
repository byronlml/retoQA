from behave import *
from src.pages.login.login import LoginPage
from src.config import config


@given('I open the saucedemo page')
def open_page(context):
    context.driver.get(config("BASE_URL"))


@when('Enter username "{username}" and password "{password}"')
def login_user(context, username, password):
    LoginPage(context.driver).login_user(username, password)


@then('Click on login button')
def click_button(context):
    LoginPage(context.driver).login_button()
    actual_title = LoginPage(context.driver).get_title()
    expected_title = "Swag Labs"
    assert actual_title == expected_title, f"El título de la página es incorrecto. Se esperaba '{expected_title}', pero se obtuvo '{actual_title}'."
