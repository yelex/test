import requests

class Singleton(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(Singleton, cls).__new__(cls)
    return cls.instance
    
class Global(Singleton):
    def __init__(self):
        self.request_session = None
        self.tor_session = None
        self.is_tor_vprok = False
        self.is_tor_globus = False

        self._set_request_session()
        self._set_tor_session()

    def _set_request_session(self):
        self.request_session = requests.session()

    def _set_tor_session(self):
        self.tor_session = requests.session()
        self.tor_session.proxies = {}
        self.tor_session.proxies['http']='socks5h://localhost:9050'
        self.tor_session.proxies['https']='socks5h://localhost:9050'

    def set_session(self, new_session):
        self.session = new_session

    def set_is_tor_vprok(self, is_tor: bool):
        self.is_tor_vprok = is_tor

    def set_is_tor_globus(self, is_tor: bool):
        self.is_tor_globus = is_tor
