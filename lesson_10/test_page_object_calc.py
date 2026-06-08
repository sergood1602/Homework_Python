import pytest
from selenium import webdriver
from Pages.CalculatorPage import CalculatorPage
import allure
from allure_commons.types import Severity


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест работы калькулятора с задержкой")
@allure.description(
    "Проверяет, что калькулятор корректно складывает 7 и 8 "
    "с установленной задержкой 45 секунд"
)
@allure.feature("Калькулятор")
@allure.severity(Severity.CRITICAL)
def test_calculator(driver):
    with allure.step("Открыть страницу калькулятора"):
        driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator = CalculatorPage(driver)

    with allure.step("Установить задержку 45 секунд"):
        calculator.enter_delay("45")

    with allure.step("Ввести число 7"):
        calculator.click_button("7")

    with allure.step("Нажать кнопку '+'"):
        calculator.click_button("+")

    with allure.step("Ввести число 8"):
        calculator.click_button("8")

    with allure.step("Нажать кнопку '='"):
        calculator.click_button("=")

    with allure.step("Проверить результат вычисления"):
        result = calculator.get_result("15")

    with allure.step(
        "Проверка: результат должен быть True "
        "(ожидаемый текст '15' появился)"
    ):
        assert result, (
            "Ожидалось, что результат будет True, но получен False. "
            "Текст '15' не появился на экране калькулятора."
        )
