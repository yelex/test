import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import os

os.chmod('./chromedrivers/chromedriver', 0o755)

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
        self._set_webdriver() # return when globus will be repaired

    def _set_request_session(self):
        self.request_session = requests.session()

    def _set_tor_session(self):
        self.tor_session = requests.session()
        self.tor_session.proxies = {}
        self.tor_session.proxies["http"] = "socks5h://localhost:9050"
        self.tor_session.proxies["https"] = "socks5h://localhost:9050"

    def _set_webdriver(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) ' \
              'Chrome/123.0.0.0 Safari/537.36'

        options = Options()

        options.add_argument("--headless");
        options.add_argument("--window-size=1920,1080");
        options.add_argument("--no-sandbox");
        options.add_argument("--disable-extensions");
        options.add_argument("--dns-prefetch-disable");
        options.add_argument("--disable-gpu");
        options.add_argument(f'user-agent={user_agent}')
        options.add_experimental_option(
        "prefs", {
            # block image loading
            "profile.managed_default_content_settings.images": 2,
        }
    )
        self.webdriver =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    def set_session(self, new_session):
        self.session = new_session

    def set_is_tor_vprok(self, is_tor: bool):
        self.is_tor_vprok = is_tor

    def set_is_tor_globus(self, is_tor: bool):
        self.is_tor_globus = is_tor
