from update_ip import renew_tor_ip
from platform import platform

def update_session():
    password = 'mypassword' if 'mac' in platform() else 'password'
    renew_tor_ip(password=password)