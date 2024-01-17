from stem import Signal
from stem.control import Controller
import time
from platform import platform
from ip import get_ip_info

def renew_tor_ip():
    password = 'mypassword' if 'mac' in platform() else 'password'
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password=password)
        controller.signal(Signal.NEWNYM)      
        
if __name__ == "__main__":
    for i in range(5):
        renew_tor_ip()
        get_ip_info()
        time.sleep(5)