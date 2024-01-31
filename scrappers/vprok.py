from bs4 import BeautifulSoup
import sys
import os
import re
import time

sys.path.insert(0, os.path.abspath('./'))

from utils.ip import update_tor_ip, print_ip
from utils.tools import wspex, wspex_space
from utils.constants import HEADERS, TIMEOUT
from globals.global_state import Global


# from get_fake_headers import get_headers


# TODO: прописать Singleton

classes = dict()
classes['title'] = ['h1', 'Title_title__nvodu']
classes['price_regular'] = ['span', 'Price_price__QzA8L Price_size_XL__MHvC1 Price_role_regular__X6X4D']
classes['price_discount'] = ['span', 'Price_price__QzA8L Price_size_XL__MHvC1 Price_role_discount__l_tpE']
classes['price_old'] = ['span', 'Price_price__QzA8L Price_size_XS__ESEhJ Price_role_old__r1uT1']

global_ = Global()

def get_data_from_link(link, global_=global_,
                       headers=HEADERS, timeout=TIMEOUT):
    '''
    Сделать сессию вовне
    Если ошибка - возвращать False, инициировать сессию с тор и возвращать сюда же
    '''

    if global_.is_tor_vprok:
        print(global_.tor_session)
        r = global_.tor_session.get(link, headers=headers, timeout=timeout)
    else:
        print(link + '\n')
        r = global_.request_session.get(link, headers=headers, timeout=timeout)

    soup = BeautifulSoup(r.text, "html.parser")
    # print(soup)
    # while 'Если считаете, что произошла ошибка' in soup.text:
    while 'Ваш ID запроса к ресурсу' in soup.text or soup.find('span', {'class': 'UiLayoutPageEmpty_contactsSecondaryText__erIsZ'}) is not None:
        # print(soup.text)
        try:
            if not global_.is_tor_vprok:
                print('i set is_tor_vprok')
                global_.is_tor_vprok = True
                print('Global().is_tor_vprok: ', global_.is_tor_vprok)
            update_tor_ip()
            print_ip(is_tor = True)
            print('we are blocked')
            print(global_.tor_session.proxies)
            r = global_.tor_session.get(link, headers=headers, timeout=timeout)
            # print(r.content)
            soup = BeautifulSoup(r.text, "html.parser")
            if not soup.find(classes['title'][0], {'class': classes['title'][-1]}):
                print('  Нет названия, пробую другой IP\n')
                continue
        except Exception as e:
            print(e)
    
    title_div = soup.find(classes['title'][0], {'class': classes['title'][-1]})
    if not title_div:
        print('  Нет названия\n')
        return False
    
    title = wspex_space(title_div.text)

    if ('Временно' in soup.text) or ('Распродано' in soup.text):
        print(f'  Распродано: {title}\n')
        return False

    price_regular_div = soup.find(classes['price_regular'][0], {'class': classes['price_regular'][-1]})

    if not price_regular_div:
        # discount
        price_new_div = soup.find(classes['price_discount'][0], {'class': classes['price_discount'][-1]})
        price_old_div = soup.find(classes['price_old'][0], {'class': classes['price_old'][-1]})
        price_new = float(re.search(r'\d+\.*\d+', wspex(price_new_div.text).replace(',', '.'))[0])
        price_old = float(re.search(r'\d+\.*\d+', wspex(price_old_div.text).replace(',', '.'))[0])
        
    else:
        price_new = float(re.search(r'\d+\.*\d+', wspex(price_regular_div.text).replace(',', '.'))[0])
        price_old = ''
    return {'site_title': title, 'price_new': price_new, 'price_old': price_old}

if __name__ == '__main__':
    link = 'https://www.vprok.ru/product/mandariny-marokko-1kg--314636'
    print(get_data_from_link(link))


    