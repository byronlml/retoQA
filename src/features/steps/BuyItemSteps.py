from behave import *


@when('Click on login button')
def click_button(self):
    self.driver.find_element("id", "login-button").click()


@when('I click on add card button')
def card(self):
    self.driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()


@when('I click on shopping cart icon')
def shopping(self):
    self.driver.find_element("id", "shopping_cart_container").click()


@when('I click on checkout')
def checkout(self):
    self.driver.find_element("id", "checkout").click()


@when('I complete the form')
def form(self):
    self.driver.find_element("id", "first-name").send_keys("BAYRON")
    self.driver.find_element("id", "last-name").send_keys("OROZCO")
    self.driver.find_element("id", "postal-code").send_keys("77022")


@when('I click on the continue button')
def continue_button(self):
    self.driver.find_element("id", "continue").click()


@when('I click on the finish button')
def finish(self):
    self.driver.find_element("id", "finish").click()


@then('should show the message thank you for your purchase')
def purchase(self):
    text = self.driver.find_element("xpath", "//*[@id='checkout_complete_container']/h2").text
    assert text == "THANK YOU FOR YOUR ORDER"






