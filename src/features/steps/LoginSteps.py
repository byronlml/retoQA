from behave import *
from src.Helper.SeleniumHelper import SeleniumHelper

url = "https://www.saucedemo.com/"


@when('I open the saucedemo page')
def get_url(self):
    SeleniumHelper(self.driver).open_url(url)


@when('Enter username "{user}" and password "{password}"')
def step_impl(self, user, password):
    self.driver.find_element("id", "user-name").send_keys(user)
    self.driver.find_element("id", "password").send_keys(password)


@then('Click on login button')
def click_button(self):
    self.driver.find_element("id", "login-button").click()


