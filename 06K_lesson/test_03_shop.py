import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_total_cost(browser):
    browser.get('https://www.saucedemo.com/')
    browser.maximize_window()

    username = browser.find_element(By.ID, 'user-name')
    password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login-button')

    username.send_keys('standard_user')
    password.send_keys('secret_sauce')
    login_button.click()

    browser.find_element(
        By.XPATH, "//button[@data-test="
        "'add-to-cart-sauce-labs-backpack']").click()
    browser.find_element(
        By.XPATH, "//button[@data-test="
        "'add-to-cart-sauce-labs-bolt-t-shirt']").click()
    browser.find_element(
        By.XPATH, "//button[@data-test="
        "'add-to-cart-sauce-labs-onesie']").click()

    browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    browser.find_element(By.ID, 'checkout').click()

    browser.find_element(By.ID, 'first-name').send_keys('Сергей')
    browser.find_element(By.ID, 'last-name').send_keys('Костромин')
    browser.find_element(By.ID, 'postal-code').send_keys('188900')

    browser.find_element(By.ID, 'continue').click()

    total_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, 'summary_total_label')))
    total_value = total_element.text
    assert total_value == "Total: $58.29"
