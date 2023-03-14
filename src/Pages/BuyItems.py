from src.Locators.BuyItems import BuyItems
from src.Helper.SeleniumHelper import SeleniumHelper
from selenium.webdriver.common.by import By


class BuyItem:
    def __init__(self, driver):
        self.driver = driver
        self.loc_buy = BuyItems()
        self.helper = SeleniumHelper(self.driver)

    def add_card_1(self):
        user = self.driver.find_element(By.ID, self.loc_buy.add_card_1_id)
        user.click()

    def add_card_2(self):
        user = self.driver.find_element(By.ID, self.loc_buy.add_card_2_id)
        user.click()

    def shipping(self):
        user = self.driver.find_element(By.ID, self.loc_buy.shopping_card_icon_id)
        user.click()

    def checkout(self):
        user = self.driver.find_element(By.ID, self.loc_buy.checkout_id)
        user.click()

    def first_name(self, first_name):
        user = self.driver.find_element(By.ID, self.loc_buy.first_name_id)
        user.clear()
        user.send_keys(first_name)

    def last_name(self, last_name):
        user = self.driver.find_element(By.ID, self.loc_buy.second_name_id)
        user.clear()
        user.send_keys(last_name)

    def postal_code(self, postal_code):
        user = self.driver.find_element(By.ID, self.loc_buy.code_postal_id)
        user.clear()
        user.send_keys(postal_code)

    def click_continue(self):
        user = self.driver.find_element(By.ID, self.loc_buy.continue_id)
        user.click()

    def finish(self):
        user = self.driver.find_element(By.ID, self.loc_buy.finish_id)
        user.click()

    def verify_buy(self):
        return self.driver.find_element(By.XPATH, self.loc_buy.compare_h2_xpath).text

    def menu(self):
        user = self.driver.find_element(By.ID, self.loc_buy.menu_button_id)
        user.click()

    def logout(self):
        user = self.driver.find_element(By.ID, self.loc_buy.logout_button_id)
        user.click()
