# Setup and teardown code retrieved from
# https://github.com/saucelabs-training/w3c-examples/blob/master/python/
# test_unittest_chrome.py
import os
import unittest

from selenium import webdriver


LOCAL_HOST = 'http://127.0.0.1:8000/'


class TestMapPage(unittest.TestCase):

    def setUp(self):
        sauce_username = os.environ["SAUCE_USERNAME"]
        sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
        remote_url = "http://{}:{}@ondemand.saucelabs.com/wd/hub".\
            format(sauce_username, sauce_access_key)

        sauceOptions = {
            "screenResolution": "1280x768",
            "platformName": "Windows 10",
            "browserVersion": "61.0",
            "seleniumVersion": "3.11.0",
            'name': 'Unittest Chrome W3C Sample'
        }

        chromeOpts = {
            'platformName': "Windows 10",
            'browserName': "chrome",
            'browserVersion': '61.0',
            'goog:chromeOptions': {'w3c': True},
            'sauce:options': sauceOptions
        }

        self.driver = webdriver.Remote(remote_url,
                                       desired_capabilities=chromeOpts)

    def tearDown(self):
        self.driver.quit()

    def test_map_page_layout(self):
        self.driver.get(LOCAL_HOST + 'map_page/')

        gm = self.driver.find_element_by_id("googleMapResults")
        self.assertFalse(gm is None)

        mp = self.driver.find_element_by_id("map")
        self.assertFalse(mp is None)

        hm = self.driver.find_element_by_id("homeButton")
        self.assertFalse(hm is None)

    def test_map_page_results_not_none(self):
        self.driver.get(LOCAL_HOST + 'map_page/')

        gm = self.driver.find_element_by_id("googleMapResults")
        self.assertFalse(gm is None)

        # Get table entries and assert the length is >= 1
        self.assertFalse(True)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.\
        loadTestsFromTestCase(TestMapPage)
    unittest.TextTestRunner().run(suite)
