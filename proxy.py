
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
from bs4 import BeautifulSoup
import platform
from io import StringIO


CHROMEDRIVER_PATH_LINUX = r'/usr/bin/chromedriver'
CHROMEDRIVER_PATH_WIN = r'C:\Users\ВТБ\Downloads\chromedriver.exe'

TEST_URL = "https://www.vprok.ru/product/iz-vologdy-iz-volog-maslo-krest-sliv-72-5-fol-180g--307205"

def _get_chromedriver_path() -> str:
	is_win = 'Windows' in platform.platform()
	return CHROMEDRIVER_PATH_LINUX if not is_win else CHROMEDRIVER_PATH_WIN
	
def _get_webdriver_chrome(proxy = '') -> webdriver.Chrome:
	chromedriver_path = _get_chromedriver_path()
	service = Service(executable_path=chromedriver_path)
	options = webdriver.ChromeOptions()
	options.add_argument('--no-sandbox')
	options.add_argument("--headless=new")
	options.add_argument("start-maximized")
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	options.add_experimental_option('useAutomationExtension', False)
	if proxy != '':
		options.add_argument(f'--proxy-server={proxy}')

	return webdriver.Chrome(options=options, service=service)

def _get_soup_delay(driver: webdriver.Chrome) -> time.sleep:
	soup = BeautifulSoup(driver.page_source, 'html.parser')
	if 'Выполняется проверка' in soup.text:
		print('Выполняется проверка...')
		time.sleep(10)

def get_proxies() -> list:
	driver = _get_webdriver_chrome()
	driver.get("https://sslproxies.org/")
	time.sleep(5)
	soup = BeautifulSoup(driver.page_source, 'html.parser')
	table = soup.find('table')
	df = pd.read_html(StringIO(str(table)))[0]
	proxies = df.loc[:,'IP Address'] + ":" + df.loc[:,'Port'].astype(str)
	driver.quit()
	return proxies.values

def get_working_proxy(url = TEST_URL) -> str:
	proxies = get_proxies()
	for i in range(0, len(proxies)):
		try:
			print("Proxy selected: {}".format(proxies[i]))
			driver = _get_webdriver_chrome(proxy=proxies[i])
			driver.get("https://www.vprok.ru/")
			_get_soup_delay(driver)
			driver.get(url)
			print(driver.title)
			print(BeautifulSoup(driver.page_source, 'lxml'))
			if WebDriverWait(driver, 10).until(EC.title_contains('Масло')):
				print(driver.title)
				print("Proxy Invoked")
				break	
		except Exception:
			driver.quit()

if __name__ == "__main__":
	print(get_working_proxy())


