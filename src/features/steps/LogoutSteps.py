from behave import *
import time


@when('I click on the menu button')
def menu(self):
    self.driver.find_element("id", "react-burger-menu-btn").click()
    time.sleep(5)


@when('I click on logout button')
def logout(self):
    logout = self.driver.find_element("xpath", "//*[@id='logout_sidebar_link']")
    logout.click()


@then('should show the page login')
def login_page(self):
    self.driver.current_url
    if self.driver.current_url == "https://www.saucedemo.com/":
        print("User logout")
