from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    def __init__(self, driver):
        """
        Конструктор класса CartPage инициализирует драйвер и создает
        объект WebDriverWait с таймаутом 10 секунд.
        :param driver: WebDriver — объект Selenium WebDriver.
        :return: None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        """
        Находит кнопку оформления заказа (checkout) по идентификатору
        "checkout" и выполняет клик по ней.
        :param: Нет (кроме self).
        :return: None.
        """
        checkout_button = self.driver.find_element(By.ID, 'checkout')
        checkout_button.click()
