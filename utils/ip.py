from global_state import Global
import json

def print_ip(is_tor=True):
    session = Global().tor_session if is_tor else Global().request_session
    json_ip = session.get('https://httpbin.org/ip').text
    ip = json.loads(json_ip)['origin']
    print(f"{'Tor IP' if is_tor else 'IP'}: {ip}")

def get_ip_info():
    print_ip(is_tor=True)
    print_ip(is_tor=False)

if __name__ == '__main__':
    get_ip_info()