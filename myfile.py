from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import re

service = Service(executable_path=r'/usr/bin/chromedriver')
options = webdriver.ChromeOptions()

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service, 
				options=options)

driver.get("https://www.vprok.ru/product/miratorg-mirat-steyk-iz-sheyk-sv-gzms400g--393530")
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup)
driver.quit()
