from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.result_locator = (By.CSS_SELECTOR, "div.screen")

    def enter_delay(self, term):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(term)

    def click_button(self, button_text):
        button = self.driver.find_element(
            By.XPATH,
            f"//span[contains(@class, 'btn') and text()='{button_text}']")
        button.click()

    def get_result(self, expected_result):
        result_element = WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(
                (self.result_locator), expected_result))
        return result_element
