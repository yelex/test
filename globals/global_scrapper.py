import numpy as np
import time
import datetime
import pandas as pd
import sys
import os
from tqdm import tqdm

print(os.path.abspath('./'))
sys.path.insert(0, os.path.abspath('./'))
from utils.constants import URLS
from global_state import Global
from scrappers import vprok

urls_vprok = URLS.loc[URLS.site_link.str.contains('vprok'), 'site_link']

data = []
global_ = Global()

for link in tqdm(urls_vprok):
    time.sleep(np.abs(np.random.randn())*3)
    print('\nglobal scrapper Global is vprok', global_.is_tor_vprok)
    vprok_data = vprok.get_data_from_link(link, global_ = global_)
    if vprok_data:
        print({'date': datetime.datetime.now().date(),
                    'category_id': URLS.loc[URLS['site_link']==link, 'category_id'].values[0],
                    'site_code': 'vprok',
                    'site_title': vprok_data['site_title'],
                    'site_link': link,
                    'price_new': vprok_data['price_new'],
                    'price_old': vprok_data['price_old']})
        data.append({'date': datetime.datetime.now().date(),
                    'category_id': URLS.loc[URLS['site_link']==link, 'category_id'].values[0],
                    'site_code': 'vprok',
                    'site_title': vprok_data['site_title'],
                    'site_link': link,
                    'price_new': vprok_data['price_new'],
                    'price_old': vprok_data['price_old']})

pd.DataFrame.from_records(data=data).to_csv('data.csv')