from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PaybrightHomePage:
    URL = 'https://www.paybright.com'
    SEARCH_INPUT = (By.NAME, 'search')
    SEARCH_RESULT = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[2]/p[2]")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

    def merchant_list_contains(self, phrase):
        search_result = self.browser.find_element(*self.SEARCH_RESULT)
        print(search_result.text)
        if search_result.text == phrase:
            return "True"
        else:
            return "False"
