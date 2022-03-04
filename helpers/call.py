import allure
import requests


from helpers import api




@allure.step("Get all todo items")
def get_todos(client=requests):
    return api.get(client, "/todos")


@allure.step("Get 1st Todo item")
def get_1st_todo(client=requests):
    return api.get(client, "/todos/1")


@allure.step("Generate Token")
def generate_token(client=requests):
    body = {"portalDeviceGuid": "DCFD38CE-60DD-4951-A2C7-4EB3DBC516F9", "phoneNumber": "4168809871", "culture": "en"}
    return api.post(client, "/Authentication/GetToken", body)


@allure.step("validate user")
def validate_user(client=requests, **kwargs):
    body = "{'pin' : '000000'}"
    return api.post(client, "/Authentication/ValidateOneTimePin", data=body)
