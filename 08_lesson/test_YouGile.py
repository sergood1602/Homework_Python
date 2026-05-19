import requests
import pytest

key = ""
url = "https://ru.yougile.com/api-v2"
my_headers = {
    "Authorization": f"Bearer {key}", "Content-Type": "application/json"}


# создать проект
def test_create_positive():
    body = {"title": "Старый проект"}
    result = requests.post(
        url=f"{url}/projects", headers=my_headers, json=body)
    assert result.status_code == 201
    response = result.json()
    return response["id"]


id = test_create_positive()


# создать проект без названия
def test_create_negative():
    body = {"title": ""}
    result = requests.post(
        url=f"{url}/projects", headers=my_headers, json=body)
    assert result.status_code == 400


# изменить проект по id
def test_update_positive():
    body = {"title": "Новый проект"}
    result = requests.put(
        url=f"{url}/projects/{id}", headers=my_headers, json=body)
    assert result.status_code == 200
    response = result.json()
    return response["id"]


new_id = test_update_positive()


# изменить проект по id с ошибочным url
def test_update_negative():
    body = {"title": "Новый проект"}
    result = requests.put(
        url=f"{url}/projects/{'id'}", headers=my_headers, json=body)
    assert result.status_code == 404


# получить проект по new_id
def test_get_project_positive():
    result = requests.get(
        url=f"{url}/projects/{new_id}", headers=my_headers)
    assert result.status_code == 200
    response = result.json()
    title = response["title"]
    assert title == "Новый проект"


# получить проект по new_id с ошибочным url
def test_get_project_negative():
    result = requests.get(
        url=f"{url}/projects/{'new_id'}", headers=my_headers)
    assert result.status_code == 404
