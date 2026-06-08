from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage инициализирует драйвер,
        создает объект WebDriverWait с таймаутом 10 секунд и находит
        все необходимые элементы на странице оформления заказа.
        :param driver: WebDriver — объект Selenium WebDriver.
        :return: None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name = self.driver.find_element(By.ID, 'first-name')
        self.last_name = self.driver.find_element(By.ID, 'last-name')
        self.postal_code = self.driver.find_element(By.ID, 'postal-code')
        self.continue_button = self.driver.find_element(By.ID, 'continue')

    def enter_first_name(self, first_name):
        """
        Вводит имя в поле ввода "first-name".
        :param first-name: str (строковое значение имени пользователя).
        :return: None.
        """
        self.first_name.send_keys(first_name)

    def enter_last_name(self, last_name):
        """
        Вводит фамилию в поле ввода "last_name".
        :param last_name: str (строковое значение фамилии пользователя).
        :return: None.
        """
        self.last_name.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        """
        Вводит почтовый индекс в поле ввода "postal-code".
        :param postal_code: str (строковое значение почтового индекса).
        :return: None.
        """
        self.postal_code.send_keys(postal_code)

    def click_continue_button(self):
        """
        Выполняет клик по кнопке "Continue".
        :param: Нет (кроме self).
        :return: None.
        """
        self.continue_button.click()

    def complete_order(self):
        """
        Ожидает появления элемента с общей суммой заказа (до 20 секунд)
        и возвращает его текстовое содержимое.
        :param: Нет (кроме self).
        :return: str (текст элемента с общей суммой).
        """
        total_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'summary_total_label')))
        return total_element.text
