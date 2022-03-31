import allure
from helpers import call as posts
from helpers.allure import allureHelper
import pytest
from base.baseclass import webbaseclass
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures("web_setup")
class TestWeb(webbaseclass):

    @pytest.mark.WEB
    @allure.step("Webpage Screenshot Test")
    def test_web(self):
        self.driver.get("https://www.google.com")
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Test Pass",
            attachment_type=AttachmentType.PNG,
        )
