from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge(service=EdgeService(
EdgeChromiumDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 10)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '[name="first-name"]')))
first_name.send_keys("Иван")
last_name = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '[name="last-name"]')))
last_name.send_keys("Петров")
address = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '[name="address"]')))
address.send_keys("Ленина, 55-3")
email = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '[name="e-mail"]')))
email.send_keys("test@skypro.com")
phone_number = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '[name="phone"]')))
phone_number.send_keys("+7985899998787")
city = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '[name="city"]')))
city.send_keys("Москва")
country = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '[name="country"]')))
country.send_keys("Россия")
job = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '[name="job-position"]')))
job.send_keys("QA")
company = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '[name="company"]')))
company.send_keys("SkyPro")
submit = wait.until(
    EC.visibility_of_element_located((By.TAG_NAME, "button"))).click()


def test_zip_code_is_red():
    zip_code_element = wait.until(EC.visibility_of_element_located((
        By.ID, "zip-code")))
    zip_code_color = zip_code_element.value_of_css_property("background-color")
    expected_color = "rgba(248, 215, 218, 1)"
    assert zip_code_color == expected_color


def test_first_name_is_green():
    first_name_element = wait.until(EC.visibility_of_element_located((
        By.ID, "first-name")))
    first_name_color = first_name_element.value_of_css_property(
        "background-color")
    expected_color = "rgba(209, 231, 221, 1)"
    assert first_name_color == expected_color


def test_last_name_is_green():
    last_name_element = wait.until(EC.visibility_of_element_located((
        By.ID, "last-name")))
    last_name_color = last_name_element.value_of_css_property(
        "background-color")
    expected_color = "rgba(209, 231, 221, 1)"
    assert last_name_color == expected_color


def test_address_is_green():
    address_element = wait.until(EC.visibility_of_element_located((
        By.ID, "address")))
    address_color = address_element.value_of_css_property("background-color")
    expected_color = "rgba(209, 231, 221, 1)"
    assert address_color == expected_color


def test_email_is_green():
    email_element = wait.until(EC.visibility_of_element_located((
        By.ID, "e-mail")))
    email_color = email_element.value_of_css_property("background-color")
    expected_color = "rgba(209, 231, 221, 1)"
    assert email_color == expected_color


def test_phone_number_is_green():
    phone_number_element = wait.until(EC.visibility_of_element_located((
        By.ID, "phone")))
    phone_number_color = phone_number_element.value_of_css_property(
        "background-color")
    expected_color = "rgba(209, 231, 221, 1)"
    assert phone_number_color == expected_color


def test_city_is_green():
    city_element = wait.until(EC.visibility_of_element_located((
        By.ID, "city")))
    city_color = city_element.value_of_css_property("background-color")
    expected_color = "rgba(209, 231, 221, 1)"
    assert city_color == expected_color


def test_country_is_green():
    country_element = wait.until(EC.visibility_of_element_located((
        By.ID, "country")))
    country_color = country_element.value_of_css_property("background-color")
    expected_color = "rgba(209, 231, 221, 1)"
    assert country_color == expected_color


def test_job_is_green():
    job_element = wait.until(EC.visibility_of_element_located((
        By.ID, "job-position")))
    job_color = job_element.value_of_css_property("background-color")
    expected_color = "rgba(209, 231, 221, 1)"
    assert job_color == expected_color


def test_company_is_green():
    company_element = wait.until(EC.visibility_of_element_located((
        By.ID, "company")))
    company_color = company_element.value_of_css_property("background-color")
    expected_color = "rgba(209, 231, 221, 1)"
    assert company_color == expected_color
