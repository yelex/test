from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

import os

print(os.listdir())

service = Service(executable_path='./chromedrivers/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://online.globus.ru/products/kotlety-kurinye-petruxa-master-domashnie-s-gribami-i-syrom-450-g-729995_ST")
soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup)