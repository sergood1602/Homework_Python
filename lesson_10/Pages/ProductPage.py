from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class ProductPage:
    def __init__(self, driver):
        """
        Конструктор класса ProductPage инициализирует драйвер
        и создает объект WebDriverWait с таймаутом 10 секунд.
        :param driver: WebDriver — объект Selenium WebDriver.
        :return: None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self):
        """
        Находит кнопку добавления рюкзака в корзину
        и выполняет клик по ней.
        :param: Нет (кроме self).
        :return: None.
        """
        backpack_button = self.driver.find_element(
            By.XPATH, "//button[@data-test="
            "'add-to-cart-sauce-labs-backpack']")
        backpack_button.click()

    def add_shirt(self):
        """
        Находит кнопку добавления футболки в корзину
        и выполняет клик по ней.
        :param: Нет (кроме self).
        :return: None.
        """
        shirt_button = self.driver.find_element(
            By.XPATH, "//button[@data-test="
            "'add-to-cart-sauce-labs-bolt-t-shirt']")
        shirt_button.click()

    def add_onesie(self):
        """
        Находит кнопку добавления комбинезона в корзину
        и выполняет клик по ней.
        :param: Нет (кроме self).
        :return: None.
        """
        onesie_button = self.driver.find_element(
            By.XPATH, "//button[@data-test="
            "'add-to-cart-sauce-labs-onesie']")
        onesie_button.click()

    def click_cart_link(self):
        """
        Находит иконку корзины и выполняет
        клик по ней для перехода в корзину.
        :param: Нет (кроме self).
        :return: None.
        """
        cart_link_button = self.driver.find_element(
            By.CLASS_NAME, 'shopping_cart_link')
        cart_link_button.click()
