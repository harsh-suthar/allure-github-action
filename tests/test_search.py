from base.baseclass import webbaseclass
from helpers.image import imageprocess


class TestClass(webbaseclass):

    def test_merchant_search(self):
        obj = imageprocess(self.driver)
        obj.screenshot('https://paybright.com/en', 'base')
        obj.screenshot('https://paybright.com/en','actual')
        obj.analyze('en_base.png', 'en_actual.png')
