import unittest
import time
from selenium import webdriver

__author__ = 'Petar'


class TestCaseGames(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_01(self):
        driver = self.driver
        driver.get("http://www.4pda.ru")
        print driver.title
        time.sleep(6)

    def tearDown(self):
        self.driver.quit()
