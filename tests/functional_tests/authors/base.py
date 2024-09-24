from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_chrome_browser
from selenium.webdriver.common.by import By
import time


class AuthorsBaseTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def sleep(self, seconds=5):
        time.sleep(seconds)

    def get_by_placeholder(self, web_element, placeholder):
        return web_element.find_element(By.XPATH, f'//input[@placeholder="{placeholder}"]')
