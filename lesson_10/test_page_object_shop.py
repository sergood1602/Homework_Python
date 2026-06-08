import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage
from Pages.CartPage import CartPage
from Pages.CheckoutPage import CheckoutPage
import allure
from allure_commons.types import Severity


@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка итоговой суммы в корзине")
@allure.description(
    "Тест проверяет, что итоговая сумма заказа из трех товаров "
    "(рюкзак, футболка, комбинезон) корректно рассчитывается "
    "и отображается на странице оформления заказа"
)
@allure.feature("Оформление заказа")
@allure.severity(Severity.CRITICAL)
def test_checkout_total(browser):
    with allure.step("Открыть главную страницу магазина"):
        browser.get("https://www.saucedemo.com")

    with allure.step("Авторизация в системе"):
        login_page = LoginPage(browser)

    with allure.step("Ввести имя пользователя"):
        login_page.enter_username("standard_user")

    with allure.step("Ввести пароль"):
        login_page.enter_password("secret_sauce")

    with allure.step("Нажать кнопку 'Login'"):
        login_page.click_login()

    with allure.step("Добавление товаров в корзину"):
        product_page = ProductPage(browser)

    with allure.step("Добавить рюкзак"):
        product_page.add_backpack()

    with allure.step("Добавить футболку"):
        product_page.add_shirt()

    with allure.step("Добавить комбинезон"):
        product_page.add_onesie()

    with allure.step("Перейти в корзину"):
        product_page.click_cart_link()

    with allure.step("Переход к оформлению заказа"):
        shopping_cart_page = CartPage(browser)

    with allure.step("Нажать кнопку 'Checkout'"):
        shopping_cart_page.click_checkout()

    with allure.step("Заполнение информации о покупателе"):
        checkout_page = CheckoutPage(browser)

    with allure.step("Ввести имя"):
        checkout_page.enter_first_name("Сергей")

    with allure.step("Ввести фамилию"):
        checkout_page.enter_last_name("Костромин")

    with allure.step("Ввести почтовый индекс"):
        checkout_page.enter_postal_code("188900")

    with allure.step("Нажать кнопку 'Continue'"):
        checkout_page.click_continue_button()

    with allure.step("Проверка итоговой суммы"):
        with allure.step("Получить итоговую сумму заказа"):
            total = checkout_page.complete_order()

    with allure.step("Проверка: итоговая сумма должна быть равна '$58.29'"):
        assert total == "Total: $58.29", (
            f"Ожидалась сумма'Total: $58.29', но получена '{total}'"
        )
