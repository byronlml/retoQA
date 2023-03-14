import time
from behave import *
from src.Helper.SeleniumHelper import SeleniumHelper
from src.Pages.Login import LoginPage

url = "https://www.saucedemo.com/"


@given('I open the saucedemo page')
def get_url(self):
    SeleniumHelper(self.driver).open_url(url)


@when('Enter username "{user}" and password "{password}"')
def step_impl(self, username, password):
    LoginPage(self.driver).username(username)
    LoginPage(self.driver).password(password)


@then('Click on login button')
def click_button(self):
    LoginPage(self.driver).login_button()
    time.sleep(1)


