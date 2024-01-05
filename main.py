import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from update_ip import renew_tor_ip, get_session
import datetime
from tools import wspex, wspex_space
import re
# from get_fake_headers import get_headers

HEADERS = {'Accept': '*/*', 
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36', 
           'Accept-Encoding': 'gzip, deflate, br', 
           'Accept-Language': 'en-US;q=0.5,en;q=0.3', 'Cache-Control': 'max-age=0', 
           'DNT': '1', 'Upgrade-Insecure-Requests': '1', 'Referer': 'https://google.com'}

TIMEOUT = 60

urls = pd.read_csv(r'./final_links.csv', index_col=0, sep=';')
urls_vprok = urls.loc[urls['site_code']=='perekrestok','site_link']
session = False

data = []

for link in urls_vprok:
    random_time = np.abs(np.random.randn())*10
    time.sleep(random_time)
    print(f'{link}')
    print('\n')
    
    classes = dict()
    classes['title'] = ['h1', 'Title_title__nvodu']
    classes['price_regular'] = ['span', 'Price_price__QzA8L Price_size_XL__MHvC1 Price_role_regular__X6X4D']
    classes['price_discount'] = ['span', 'Price_price__QzA8L Price_size_XL__MHvC1 Price_role_discount__l_tpE']
    classes['price_old'] = ['span', 'Price_price__QzA8L Price_size_XS__ESEhJ Price_role_old__r1uT1']
    if session:
        r = session.get(link, headers=HEADERS, timeout=TIMEOUT)
    else:
        r = requests.get(link, headers=HEADERS, timeout=TIMEOUT)
    soup = BeautifulSoup(r.text, "html.parser")

    while 'Если считаете, что произошла ошибка' in soup.text:
        try:
            renew_tor_ip()
            session = get_session()
            r = session.get(link, headers=HEADERS, timeout=TIMEOUT)
            soup = BeautifulSoup(r.text, "html.parser")
        except Exception as e:
            print(e)
            continue

    title_div = soup.find(classes['title'][0], {'class': classes['title'][-1]})
    if not title_div:
        print(soup, file=open('text.txt', 'w', encoding="utf-8"))
        print('  Нет названия\n')
        continue
    
    title = wspex_space(title_div.text)

    if ('Временно' in soup.text) or ('Распродано' in soup.text):
        print(f'  Распродано: {title}\n')
        continue

    price_regular_div = soup.find(classes['price_regular'][0], {'class': classes['price_regular'][-1]})

    if not price_regular_div:
        # discount
        price_new_div = soup.find(classes['price_discount'][0], {'class': classes['price_discount'][-1]})
        price_old_div = soup.find(classes['price_old'][0], {'class': classes['price_old'][-1]})
        price_new = float(re.search(r'\d+\.*\d+', wspex(price_new_div.text).replace(',', '.'))[0])
        price_new = float(re.search(r'\d+\.*\d+', wspex(price_old_div.text).replace(',', '.'))[0])
        
    else:
        price_new = float(re.search(r'\d+\.*\d+', wspex(price_regular_div.text).replace(',', '.'))[0])
        price_old = ''

    data.append({'date': datetime.datetime.now().date(),
                 'category_id': urls.loc[urls['site_link']==link, 'category_id'].values[0],
                 'site_code': 'perekrestok',
                 'site_title': title,
                 'site_link': link,
                 'price_new': price_new,
                 'price_old': price_old})
    print(f'''  title: {title}\n  price_new: {price_new}\n  price_old: {price_old}\n''')

pd.DataFrame.from_records(data=data).to_csv('data.csv')
    