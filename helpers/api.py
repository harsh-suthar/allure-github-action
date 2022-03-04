import allure
from helpers.allure import allureHelper
host_url = "https://jsonplaceholder.typicode.com"
paybright_host_url = "https://playground.portal.paybright.com/api"


def get(client, path):
    response = client.get(host_url + path)
    a = allureHelper(allure)
    a.attach_request(response)
    a.attach_response(response)
    return response


@allure.step("Execute request")
def post(client, path, body):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = paybright_host_url + path
    response = client.post(url, headers=headers, json=body)
    a = allureHelper(allure)
    a.attach_request(response)
    a.attach_response(response)
    return response
