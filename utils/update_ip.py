from stem import Signal
from stem.control import Controller
import requests
import time

def get_session():
    session = requests.session()

    # TO Request URL with SOCKS over TOR
    session.proxies = {}
    session.proxies['http']='socks5h://localhost:9050'
    session.proxies['https']='socks5h://localhost:9050'

    return session

def renew_tor_ip(password='password'):
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password=password)
        controller.signal(Signal.NEWNYM)        


if __name__ == "__main__":
    for i in range(5):
        get_session()
        renew_tor_ip()
        time.sleep(5)