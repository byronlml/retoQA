from src.Locators.Login import LocatorLogin
from src.Helper.SeleniumHelper import SeleniumHelper
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.loc_login = LocatorLogin()
        self.helper = SeleniumHelper(self.driver)

    def username(self, username):
        user = self.driver.find_element(By.ID, self.loc_login.username_id)
        user.clear()
        user.send_keys(username)

    def password(self, password):
        user = self.driver.find_element(By.ID, self.loc_login.password_id)
        user.clear()
        user.send_keys(password)

    def login_button(self):
        user = self.driver.find_element(By.ID, self.loc_login.login_button_id)
        user.click()
