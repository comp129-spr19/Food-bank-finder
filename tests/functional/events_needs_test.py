import unittest

from functional_lib.general import get_chromedriver
from functional_lib.general import kill_server
from functional_lib.general import LOCAL_HOST
from functional_lib.general import run_server


class TestStringMethods(unittest.TestCase):

    def test_events_needs_list_not_empty(self):
        # Populate DB with fake events and accompanying food banks

        # Stub latitude and longitude to be near above events

        proc = run_server()

        chrome = get_chromedriver()
        chrome.implicitly_wait(30)
        chrome.maximize_window()

        chrome.get(LOCAL_HOST + 'events_needs/')

        # el = chrome.findElementById('events_list')

        # Get list of events and assert non-zero number of entries
        self.assertFalse(True)

        kill_server(proc)


if __name__ == '__main__':
    unittest.main()
