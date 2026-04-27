from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 50)
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

delay_input = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
delay_input.clear()
delay_input.send_keys("45")

button7 = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//span[contains(@class, 'btn') and contains("
     "@class, 'btn-outline-primary') and text()='7']"))).click()

button_plus = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//span[contains(@class, 'btn') and contains("
     "@class, 'btn-outline-success') and text()='+']"))).click()

button8 = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//span[contains(@class, 'btn') and contains("
     "@class, 'btn-outline-primary') and text()='8']"))).click()

button_equal_sign = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//span[contains(@class, 'btn') and contains("
     "@class, 'btn-outline-warning') and text()='=']"))).click()


def test_screen_is_15():
    screen_element = wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "div.screen"), "15"))
    assert screen_element, "15"
