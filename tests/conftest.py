import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
import allure
from dotenv import load_dotenv
import pytest
from allure_commons.types import AttachmentType


@pytest.fixture
def web_setup(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox");
    options.add_argument("--disable-dev-shm-usage");
    options.add_argument("--headless");
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
        options=options,
    )
    driver.maximize_window()
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield driver
    if request.session.testsfailed != before_failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Test failed",
            attachment_type=AttachmentType.PNG,
        )
    driver.quit()
