from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=r'/usr/bin/chromedriver')
options = webdriver.ChromeOptions()

print("Process started")
options.add_argument('--no-sandbox')
options.add_argument("--headless=new")
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, service=service)
driver.get("https://www.vprok.ru/")
print(driver.title)