import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from utils.ip import update_tor_ip
import datetime
from utils.tools import wspex, wspex_space
from utils.constants import URLS, HEADERS, TIMEOUT
from utils.global_state import Global
import re
from sys import platform
# from get_fake_headers import get_headers


# TODO: прописать Singleton

classes = dict()
classes['title'] = ['h1', 'Title_title__nvodu']
classes['price_regular'] = ['span', 'Price_price__QzA8L Price_size_XL__MHvC1 Price_role_regular__X6X4D']
classes['price_discount'] = ['span', 'Price_price__QzA8L Price_size_XL__MHvC1 Price_role_discount__l_tpE']
classes['price_old'] = ['span', 'Price_price__QzA8L Price_size_XS__ESEhJ Price_role_old__r1uT1']

is_tor = False

def get_data_from_link(link, is_tor=is_tor, 
                       headers=HEADERS, timeout=TIMEOUT):
    '''
    Сделать сессию вовне
    Если ошибка - возвращать False, инициировать сессию с тор и возвращать сюда же
    '''
    # TODO: дописать конфиг с is_tor

    if is_tor:
        r = Global().tor_session.get(link, headers=headers, timeout=timeout)
    else:
        print('im here')
        r = Global().request_session.get(link, headers=headers, timeout=timeout)
    soup = BeautifulSoup(r.text, "html.parser")

    # while 'Если считаете, что произошла ошибка' in soup.text:
    while 'Если считаете, что произошла ошибка' in soup.text:
        try:
            if not is_tor:
                is_tor = True
            update_tor_ip()
            r = Global().tor_session.get(link, headers=headers, timeout=timeout)
            soup = BeautifulSoup(r.text, "html.parser")
        except Exception as e:
            print(e)
    
    title_div = soup.find(classes['title'][0], {'class': classes['title'][-1]})
    if not title_div:
        print(soup, file=open('text.txt', 'w', encoding="utf-8"))
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

# data = []

# for link in urls_vprok:
#     random_time = np.abs(np.random.randn())*5
#     time.sleep(random_time)
#     print(f'{link}')
#     print('\n')
    

    

#     data.append({'date': datetime.datetime.now().date(),
#                  'category_id': urls.loc[urls['site_link']==link, 'category_id'].values[0],
#                  'site_code': 'perekrestok',
#                  'site_title': title,
#                  'site_link': link,
#                  'price_new': price_new,
#                  'price_old': price_old})
#     print(f'''  title: {title}\n  price_new: {price_new}\n  price_old: {price_old}\n''')

# pd.DataFrame.from_records(data=data).to_csv('data.csv')
    