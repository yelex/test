import json
import time
from platform import platform
from stem.control import Controller
import sys
import os

sys.path.insert(0, os.path.abspath('../'))

from utils.global_state import Global

def print_ip(is_tor: bool =True) -> None:
    session = Global().tor_session if is_tor else Global().request_session
    json_ip = session.get('https://httpbin.org/ip').text
    ip = json.loads(json_ip)['origin']
    print(f"{'Tor IP' if is_tor else 'IP'}: {ip}")

def update_tor_ip() -> None:
    password = 'mypassword' if 'mac' in platform() else 'password'
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password=password)
        controller.signal("NEWNYM")

if __name__ == '__main__':
    for i in range(5):
        update_tor_ip()
        print_ip(is_tor=True)
        time.sleep(5)
