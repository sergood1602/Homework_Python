from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username = self.driver.find_element(By.ID, 'user-name')
        self.password = self.driver.find_element(By.ID, 'password')
        self.login_button = self.driver.find_element(By.ID, 'login-button')

    def enter_username(self, username):
        self.username.send_keys(username)

    def enter_password(self, password):
        self.password.send_keys(password)

    def click_login(self):
        self.login_button.click()
