from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import os


service = Service(executable_path='./chromedrivers/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://online.globus.ru/products/govyazhya-noga-na-kosti-1-upakovka-500-950-g/")

time.sleep(4)
soup = BeautifulSoup(driver.page_source, 'lxml')

print(soup.findAll('span', {'itemprop': 'name'})[-1])
