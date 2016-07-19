__author__ = 'Petar'
# file test_3.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Remote(
   command_executor='http://USERNAME:ACCESS_KEY@YOUR_SUBDOMAIN.gridlastic.com:80/wd/hub',
   desired_capabilities={
            "browserName": "firefox",
            "version": "45",
            "platform": "VISTA",
            "video": "True"
        })

driver.implicitly_wait(30)
driver.maximize_window() # If platform is Linux instead use: driver.set_window_size(1920,1080)


def test_one():
    try:
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("documentation")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
    finally:
            print "Test One - Video: " + driver.session_id
            driver.quit()