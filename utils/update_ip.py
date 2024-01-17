from stem import Signal
from stem.control import Controller
import requests
import time
import os, sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from check_ip import check_ip

def get_session():
    session = requests.session()

    # TO Request URL with SOCKS over TOR
    session.proxies = {}
    session.proxies['http']='socks5h://localhost:9050'
    session.proxies['https']='socks5h://localhost:9050'
    check_ip(session=session)
    return session

def renew_tor_ip(password='password'):
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password=password)
        controller.signal(Signal.NEWNYM)        
        

if __name__ == "__main__":
    for i in range(3):
        get_session()
        renew_tor_ip()
        time.sleep(5)