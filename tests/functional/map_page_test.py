import unittest

from functional_lib.general import get_chromedriver
from functional_lib.general import kill_server
from functional_lib.general import LOCAL_HOST
from functional_lib.general import run_server


class TestStringMethods(unittest.TestCase):

    def test_map_page_layout(self):
        proc = run_server()

        chrome = get_chromedriver()
        chrome.implicitly_wait(30)
        chrome.maximize_window()

        chrome.get(LOCAL_HOST + 'map_page/')

        gm = chrome.findElementById("google_map_results")
        self.assertFalse(gm is None)

        mp = chrome.findElementById("map")
        self.assertFalse(mp is None)

        kill_server(proc)


if __name__ == '__main__':
    unittest.main()
