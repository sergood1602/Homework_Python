from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name = self.driver.find_element(By.ID, 'first-name')
        self.last_name = self.driver.find_element(By.ID, 'last-name')
        self.postal_code = self.driver.find_element(By.ID, 'postal-code')
        self.continue_button = self.driver.find_element(By.ID, 'continue')

    def enter_first_name(self, first_name):
        self.first_name.send_keys(first_name)

    def enter_last_name(self, last_name):
        self.last_name.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.postal_code.send_keys(postal_code)

    def click_continue_button(self):
        self.continue_button.click()

    def complete_order(self):
        total_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
            (By.CLASS_NAME, 'summary_total_label')))
        return total_element.text
