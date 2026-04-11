from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

number = driver.find_element(By.TAG_NAME, "input")

number.send_keys("12345")
number.clear()
number.send_keys("54321")

driver.quit()
