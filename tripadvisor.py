# -*- coding: utf-8 -*-

import requests
import json
import traceback
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

CONFIG = json.loads(open('./config.json').read())

class Tripadvisor:

    def __init__(self):
        self.driver = self.__get_driver()

    def __enter__(self):
        
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type:
            traceback.print_exception(exc_type, exc_value, tb)

        self.driver.close()
        self.driver.quit()

        return True


    def get_urls(self, query, intput_section):

    def __get_driver(self, debug=True):
        path = CONFIG["chromedriver_path"]
        debug = CONFIG["debug"]

        if not debug:
            options.add_argument("--headless")

        options = Options()
        options.add_argument("--window-size=1366,768")
        options.add_argument("--disable-notifications")
        options.add_argument("--lang=en")
        input_driver = webdriver.Chrome(executable_path=path, chrome_options=options)

        return input_driver
