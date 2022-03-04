import allure
import requests


class allureHelper:

    def __init__(self, allure):
        self.allure = allure

    def attach_request(self, response):
        if response.request.method == 'POST':
            self.allure.attach(('{}\n{}\r\n{}\r\n\r\n{}\n{}'.format(
                '-----------POST Request Start-----------',
                response.request.method + " " + response.request.url,
                "\n".join("{}: {}".format(k, v) for k, v in response.request.headers.items()),
                "Request Body:" + '\r\n' + response.request.body.decode("utf-8"),
                '-----------POST Request End-----------',
            )), name='Post Request', attachment_type=self.allure.attachment_type.TEXT)
        else:
            self.allure.attach(('{}\n{}\r\n{}\r\n\r\n{}'.format(
                '-----------GET Request Start-----------',
                response.request.method + " " + response.request.url,
                "\n".join("{}: {}".format(k, v) for k, v in response.request.headers.items()),
                '-----------GET Request End-----------',
            )), name='Get Request', attachment_type=self.allure.attachment_type.TEXT)

    def attach_response(self, response):
        self.allure.attach(('{}\n{}\r\n{}\r\n\r\n{}\n{}'.format(
            '-----------Response Start-----------',
            "Status code:" + str(response.status_code),
            '\r\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
            "Response Body:" + '\r\n' + response.text,
            '-----------Response End-----------',
        )), name='Response', attachment_type=self.allure.attachment_type.TEXT)
