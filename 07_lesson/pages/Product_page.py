from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self):
        backpack_button = self.driver.find_element(
            By.XPATH, "//button[@data-test="
            "'add-to-cart-sauce-labs-backpack']")
        backpack_button.click()

    def add_shirt(self):
        shirt_button = self.driver.find_element(
            By.XPATH, "//button[@data-test="
            "'add-to-cart-sauce-labs-bolt-t-shirt']")
        shirt_button.click()

    def add_onesie(self):
        onesie_button = self.driver.find_element(
            By.XPATH, "//button[@data-test="
            "'add-to-cart-sauce-labs-onesie']")
        onesie_button.click()

    def click_cart_link(self):
        cart_link_button = self.driver.find_element(
            By.CLASS_NAME, 'shopping_cart_link')
        cart_link_button.click()
