import allure
from helpers import call as posts
from helpers.allure import allureHelper
import pytest

@pytest.mark.usefixtures("set_up")
class TestWeb:
    def test_odin(self,odin):
        print(odin)
        pass

    @allure.step("Test1 execution start")
    def test_get_token1(self):
        result = posts.generate_token()
        assert result.status_code == 200

    @allure.step("Test1 execution start")
    def test_get_token2(self):
        result = posts.get_1st_todo()
        assert result.status_code == 200
