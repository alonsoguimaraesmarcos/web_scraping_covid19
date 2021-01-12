# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
## web scraping site do Ministério da Saúde (COVID-19)


# Pacotes utilizados

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json




url = "https://covid.saude.gov.br/"

option = Options()
option.headless = True

#option.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome("C:/Users/marco/Downloads/chromedriver_win32/chromedriver.exe")
#não mostrar o que está sendo feito #driver = webdriver.Chrome("C:/Users/marco/Downloads/chromedriver_win32/chromedriver.exe",options=option)

driver.get(url)
time.sleep(10)

#driver.find_element_by_tag_name("button").click()

driver.find_element_by_xpath("//ion-button[@class='btn-outline md button button-solid button-has-icon-only ion-activatable ion-focusable hydrated']").click()





# Parsear o conteúdo HTML



driver.quit()