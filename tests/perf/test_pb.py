import allure

from helpers import call as posts


class TestClasss:

    @allure.step("Test1 execution start")
    def test_get_token1(self):
        result = posts.generate_token()
        assert result.status_code == 200

    @allure.step("Test1 execution start")
    def test_get_token2(self):
        result = posts.get_1st_todo()
        assert result.status_code == 200

    # @allure.step("Test2 execution start")
    # def test_get_token2(self):
    #     result = posts.generate_token()
    #     assert result.status_code == 200
    #
    # @allure.step("Test3 execution start")
    # def test_get_token3(self):
    #     result = posts.generate_token()
    #     assert result.status_code == 200
    #
    # @allure.step("Test4 execution start")
    # def test_get_token4(self):
    #     result = posts.generate_token()
    #     assert result.status_code == 200

