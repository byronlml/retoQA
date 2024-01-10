from src.locators.buy_items.buy_items import BuyItems
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BuyItemsPage:
    def __init__(self, driver):
        self.driver = driver
        self.loc_buy = BuyItems()

    def add_card_1(self):
        user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.loc_buy.add_card_1_id))
        )
        user.click()

    def add_card_2(self):
        user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.loc_buy.add_card_2_id))
        )
        user.click()

    def shipping(self):
        user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.loc_buy.shopping_card_icon_id))
        )
        user.click()

    def checkout(self):
        user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.loc_buy.checkout_id))
        )
        user.click()

    def first_name(self, first_name):
        user = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.loc_buy.first_name_id))
        )
        user.clear()
        user.send_keys(first_name)

    def last_name(self, last_name):
        user = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.loc_buy.second_name_id))
        )
        user.clear()
        user.send_keys(last_name)

    def postal_code(self, postal_code):
        user = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.loc_buy.code_postal_id))
        )
        user.clear()
        user.send_keys(postal_code)

    def complete_form(self, first_name, last_name, postal_code):
        self.first_name(first_name)
        self.last_name(last_name)
        self.postal_code(postal_code)

    def click_continue(self):
        user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.loc_buy.continue_id))
        )
        user.click()

    def finish(self):
        user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.loc_buy.finish_id))
        )
        user.click()

    def verify_buy(self):
        return self.driver.find_element(By.XPATH, self.loc_buy.compare_h2_xpath).text

    def menu(self):
        user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.loc_buy.menu_button_id))
        )
        user.click()

    def logout(self):
        user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.loc_buy.logout_button_id))
        )
        user.click()
