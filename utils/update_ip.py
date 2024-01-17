from stem import Signal
from stem.control import Controller
import time

def renew_tor_ip(password='password'):
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password=password)
        controller.signal(Signal.NEWNYM)        
        
if __name__ == "__main__":
    for i in range(5):
        renew_tor_ip()
        time.sleep(5)