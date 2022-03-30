import allure
from helpers import call as posts
from helpers.allure import allureHelper
import pytest
from base.baseclass import webbaseclass


class TestAPI:

    @allure.link('https://github.com/harsh-suthar/allure-github-action/commit/333ca228f74b0556efa4c8d9394bf29524007a3f',
                 name='Check Code Change')
    @allure.step("Generate Paybright Token")
    def test_paybright_token_api(self):
        result = posts.generate_token()
        assert result.status_code == 200

    @allure.step("Fetch Todo Items")
    def test_todo_api(self):
        result = posts.get_1st_todo()
        assert result.status_code == 200