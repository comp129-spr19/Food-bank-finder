# import platform
from subprocess import (
    Popen
)

from selenium import (
    webdriver
)


DONATE_FOOD = 'donatefood/'
LOCAL_HOST = 'http://127.0.0.1:8000/'


def get_chromedriver():
    # if platform.system() is 'Linux' or platform.system() is 'Darwin':
    return webdriver.Chrome('~/chromedriver/chromedriver.exe')
    # elif platform.system() is 'Windows':
    #     return webdriver.Chrome('C:/chromedriver')
    # else:
    #     exit(1)


def run_server():
    return Popen(['python', DONATE_FOOD + 'manage.py', 'runserver'])


def kill_server(proc):
    proc.terminate()
