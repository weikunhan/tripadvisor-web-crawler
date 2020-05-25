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
        url_list = []
        selected_section = CONFIG["section"][intput_section]

        self.driver.get(CONFIG["website"] + CONFIG["search_api"].format(query))
        wait = WebDriverWait(self.driver, CONFIG["timeout"])
        xpath_filter = '//a[@class=\'search-filter ui_tab  \'  and @data-filter-id=\'{}\']'.format(selected_section)
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath_filter))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.search-results-list')))
        response = BeautifulSoup(self.driver.page_source, 'html.parser')
        results_list = response.find_all('div', class_='result-title')
        
        for result in results_list:
            features = result['onclick'].split(',')
            url = CONFIG["website"] + features[3].lstrip()[1:-1]
            url_list.append(url)

        return url_list

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
