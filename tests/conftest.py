import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

platform_config = config.read_json("allure-github-action/tests", "config.json")
env_config = platform_config.get("Environments")

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="SANDBOX")
    parser.addoption("--odin", action="store", default="False")


@pytest.fixture
def set_up(request,odin):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--hide-scrollbars")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    print(odin)
    request.cls.driver = driver
    yield driver
    driver.quit()

    
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
