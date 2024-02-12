from src.locators.login.Login import LocatorLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.loc_login = LocatorLogin()

    def username(self, username):
        user = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.loc_login.username_id))
        )
        user.clear()
        user.send_keys(username)

    def password(self, password):
        user = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.loc_login.password_id))
        )
        user.clear()
        user.send_keys(password)

    def login_button(self):
        user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.loc_login.login_button_id))
        )
        user.click()

    def login_user(self, username, password):
        self.username(username)
        self.password(password)

    def get_title(self):
        return self.driver.title
