import allure
from helpers import call as posts
from helpers.allure import allureHelper
import pytest

@pytest.mark.usefixtures("set_up")
class TestWeb:
    def test_odin(self,odin):
        allure.attach((odin), name='Odin', attachment_type=self.allure.attachment_type.TEXT)




