import time
from platform import platform
from print_ip import print_ip
from stem.control import Controller
from stem.control import Signal


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
