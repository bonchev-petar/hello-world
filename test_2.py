import unittest
import time
from selenium import webdriver

__author__ = 'Petar'


class TestCaseNews(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_01(self):
        driver = self.driver
        title = driver.get("http://www.gsmarena.com")
        print title
        time.sleep(6)

    def tearDown(self):
        self.driver.quit()