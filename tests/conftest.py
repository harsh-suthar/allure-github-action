import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def set_up(request):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--hide-scrollbars")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()
