# Setup and teardown code retrieved from
# https://github.com/saucelabs-training/w3c-examples/blob/master/python/
# test_unittest_chrome.py
import os
import unittest

from selenium import webdriver


LOCAL_HOST = 'http://127.0.0.1:8000/'


class TestEventsNeedsPage(unittest.TestCase):

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

    def test_events_needs_list_not_empty(self):
        # Populate DB with fake events and accompanying food banks

        # Stub latitude and longitude to be near above events

        self.driver.get(LOCAL_HOST + 'events_needs/')

        el = self.driver.find_element_by_id('eventsList')
        self.assertFalse(el is None)

        # Get list of events and assert non-zero number of entries
        self.assertFalse(True)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.\
        loadTestsFromTestCase(TestEventsNeedsPage)
    unittest.TextTestRunner().run(suite)
