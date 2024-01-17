import requests

CHECK_URL = 'http://httpbin.org/ip'

def __init__():
    return

def check_ip(session=False):
    r = session.get(CHECK_URL) if session else requests.get(CHECK_URL)
    print(r.text)
