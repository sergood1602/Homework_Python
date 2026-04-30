from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    button7 = driver.find_element(
        By.XPATH, "//span[contains(@class, 'btn') and contains("
            "@class, 'btn-outline-primary') and text()='7']")
    button7.click()

    button_plus = driver.find_element(
        By.XPATH, "//span[contains(@class, 'btn') and contains("
            "@class, 'btn-outline-success') and text()='+']")
    button_plus.click()

    button8 = driver.find_element(
        By.XPATH, "//span[contains(@class, 'btn') and contains("
            "@class, 'btn-outline-primary') and text()='8']")
    button8.click()

    button_equal_sign = driver.find_element(
        By.XPATH, "//span[contains(@class, 'btn') and contains("
            "@class, 'btn-outline-warning') and text()='=']")
    button_equal_sign.click()

    screen_element = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div.screen"), "15"))
    assert screen_element, "15"

    driver.quit()
