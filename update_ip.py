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

    try:
        r = session.get('http://httpbin.org/ip')
    except Exception as e:
        print(str(e))
    else:
        print(r.text)
    return session


def renew_tor_ip():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="MyStr0n9P#D")
        controller.signal(Signal.NEWNYM)


if __name__ == "__main__":
    for i in range(5):
        get_session()
        renew_tor_ip()
        time.sleep(5)