import unittest
from subprocess import (
    Popen
)

from selenium import (
    webdriver
)


DONATE_FOOD = '../../donatefood/manage.py runserver'
LOCAL_HOST = 'http://127.0.0.1:8000/'


class TestStringMethods(unittest.TestCase):

    def test_home_page_layout(self):
        proc = run_server()

        firefox = webdriver.Firefox()
        firefox.implicitly_wait(30)
        firefox.maximize_window()

        firefox.get(LOCAL_HOST)

        en = firefox.findElementById("events_needs_button")
        self.assertFalse(en is None)

        mp = firefox.findElementById("map_page_button")
        self.assertFalse(mp is None)

        kill_server(proc)

    def test_map_page_layout(self):
        proc = run_server()

        firefox = webdriver.Firefox()
        firefox.implicitly_wait(30)
        firefox.maximize_window()

        firefox.get(LOCAL_HOST + 'map_page/')

        en = firefox.findElementById("google_map")
        self.assertFalse(en is None)

        mp = firefox.findElementById("map_page_button")
        self.assertFalse(mp is None)

        kill_server(proc)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()


# Helper Functions
def run_server():
    return Popen(['python', DONATE_FOOD + 'manage.py', 'runserver'])


def kill_server(proc):
    proc.terminate()
