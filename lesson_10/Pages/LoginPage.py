from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        """
        Конструктор класса LoginPage инициализирует драйвер,
        создает объект WebDriverWait с таймаутом 10 секунд и
        находит все необходимые элементы на странице авторизации.
        :param driver: WebDriver — объект Selenium WebDriver.
        :return: None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username = self.driver.find_element(By.ID, 'user-name')
        self.password = self.driver.find_element(By.ID, 'password')
        self.login_button = self.driver.find_element(By.ID, 'login-button')

    def enter_username(self, username):
        """
        Вводит имя пользователя в поле ввода "user-name".
        :param username: str (строковое значение имени пользователя).
        :return: None.
        """
        self.username.send_keys(username)

    def enter_password(self, password):
        """
        Вводит пароль в поле ввода "password".
        :param password: str (строковое значение пароля).
        :return: None.
        """
        self.password.send_keys(password)

    def click_login(self):
        """
        Выполняет клик по кнопке входа "login-button".
        :param: Нет (кроме self).
        :return: None.
        """
        self.login_button.click()
