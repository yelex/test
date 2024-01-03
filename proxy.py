
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
from bs4 import BeautifulSoup

service = Service(executable_path=r'/usr/bin/chromedriver')
options = webdriver.ChromeOptions()

print("Process started")
options.add_argument('--no-sandbox')
options.add_argument("--headless=new")
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, service=service)
driver.get("https://sslproxies.org/")
print(driver.title)
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')
table = soup.find('table')
df = pd.read_html(str(table))[0]
ips = df.loc[:,'IP Address']
ports = df.loc[:,'Port']
driver.quit()
proxies = []
print(ips)
print(ports)
for i in range(0, len(ips)):
	proxies.append(str(ips[i])+':'+str(ports[i]))
print(proxies)
for i in range(0, len(proxies)):
	try:
		print("Proxy selected: {}".format(proxies[i]))
		options = webdriver.ChromeOptions()
		options.add_argument("--no-sandbox")
		options.add_argument("--headless=new")
		options.add_argument("start-maximized")
		options.add_experimental_option("excludeSwitches", ["enable-automation"])
		options.add_experimental_option('useAutomationExtension', False)
		options.add_argument('--proxy-server={}'.format(proxies[i]))
		driver = webdriver.Chrome(options=options,service=service)

		driver.get("https://www.vprok.ru/product/iz-vologdy-iz-volog-maslo-krest-sliv-72-5-fol-180g--307205")
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		print(soup)

		if 'ошибка' not in soup.text:
			with open("output.txt", "a") as f:
				print(soup.text, file=f)
			break
		# if WebDriverWait(driver, 5).until(EC.title_contains('Масло')):
		# 	break
	except Exception:
		driver.quit()
print("Proxy Invoked")
