from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

username_id = "#username"
username = driver.find_element(By.CSS_SELECTOR, username_id)
username.send_keys("tomsmith")

password_id = "#password"
password = driver.find_element(By.CSS_SELECTOR, password_id)
password.send_keys("SuperSecretPassword!")

Login = driver.find_element(By.CSS_SELECTOR, "button.radius")
Login.click()

green_button_id = "div#flash.flash.success"
green_button = driver.find_element(By.CSS_SELECTOR, green_button_id)
text_from_green_button = green_button.text
print(text_from_green_button)

driver.quit()
