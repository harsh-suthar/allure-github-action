import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import allure
from dotenv import load_dotenv
import pytest
from allure_commons.types import AttachmentType
from helpers.ConfigurationReader import ConfigurationReader



config = ConfigurationReader()
platform_config = config.read_json("allure-github-action/tests", "config.json")
env_config = platform_config.get("Environments")

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="SANDBOX")
    parser.addoption("--odin", action="store", default="False")


@pytest.fixture
def set_up(request,odin):
    print(f"http://{odin}.affirm-odin.com")
    

    
@pytest.fixture(name="odin")
def fixture_odin(request):
    custom_odin = request.config.getoption("--odin")
    if custom_odin == "False":
        environment = request.config.getoption("env")
        if environment not in env_config["supported_environment"]:
            raise Exception(f'"{environment}" is not a supported environment')
        else:
            load_dotenv()
            odin_id = os.environ.get(f"{environment}_ODIN")
            return odin_id
    else:
        return custom_odin
