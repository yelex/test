from utils.global_state import Global
import json
import time
from platform import platform
from stem.control import Controller
from stem.control import Signal

def print_ip(is_tor=True):
    session = Global().tor_session if is_tor else Global().request_session
    json_ip = session.get('https://httpbin.org/ip').text
    ip = json.loads(json_ip)['origin']
    print(f"{'Tor IP' if is_tor else 'IP'}: {ip}")

def update_tor_ip():
    password = 'mypassword' if 'mac' in platform() else 'password'
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password=password)
        controller.signal(Signal.NEWNYM)  

if __name__ == '__main__':
    for i in range(5):
        update_tor_ip()
        print_ip(is_tor=True)
        time.sleep(5)
