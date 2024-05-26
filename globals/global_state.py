import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.constants import PATH_CHROMEDRIVER
import os


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class Global(Singleton):
    def __init__(self):
        self.request_session = None
        self.tor_session = None
        self.is_tor_vprok = False
        self.is_tor_globus = False
        self.webdriver = None

        self._set_request_session()
        self._set_tor_session()
        self._set_webdriver()

    def _set_request_session(self):
        self.request_session = requests.session()

    def _set_tor_session(self):
        self.tor_session = requests.session()
        self.tor_session.proxies = {}
        self.tor_session.proxies["http"] = "socks5h://localhost:9050"
        self.tor_session.proxies["https"] = "socks5h://localhost:9050"

    def _set_webdriver(self):
        os.chmod(PATH_CHROMEDRIVER, 0o755)  # for linux
        
        service = Service(executable_path=PATH_CHROMEDRIVER)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        self.webdriver = webdriver.Chrome(service=service, options=options)

    def set_session(self, new_session):
        self.session = new_session

    def set_is_tor_vprok(self, is_tor: bool):
        self.is_tor_vprok = is_tor

    def set_is_tor_globus(self, is_tor: bool):
        self.is_tor_globus = is_tor
