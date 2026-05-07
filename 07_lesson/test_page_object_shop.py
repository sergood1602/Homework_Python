import pytest
from selenium import webdriver
from pages.Login_page import LoginPage
from pages.Product_page import ProductPage
from pages.Cart_page import CartPage
from pages.Checkout_page import CheckoutPage


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_checkout_total(browser):
    browser.get("https://www.saucedemo.com")

    login_page = LoginPage(browser)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    product_page = ProductPage(browser)
    product_page.add_backpack()
    product_page.add_shirt()
    product_page.add_onesie()
    product_page.click_cart_link()

    shopping_cart_page = CartPage(browser)
    shopping_cart_page.click_checkout()

    checkout_page = CheckoutPage(browser)
    checkout_page.enter_first_name("Сергей")
    checkout_page.enter_last_name("Костромин")
    checkout_page.enter_postal_code("188900")
    checkout_page.click_continue_button()
    total = checkout_page.complete_order()
    assert total == "Total: $58.29"
