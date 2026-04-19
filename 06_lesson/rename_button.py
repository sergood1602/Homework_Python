from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://uitestingplayground.com/textinput")

element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")

content = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
driver.implicitly_wait(15)
content = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(content)

driver.quit()
