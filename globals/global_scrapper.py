import numpy as np
import time
import datetime
import pandas as pd
import sys
import os
from tqdm import tqdm
from sqlalchemy import create_engine

sys.path.insert(0, os.path.abspath('./'))
from utils.constants import URLS, DB_CONNECTION_STR
from global_state import Global
from scrappers import vprok

def main():
    db_connection = create_engine(DB_CONNECTION_STR)
    urls_vprok = URLS.loc[URLS.site_link.str.contains('vprok'), 'site_link']

    categories_df = pd.read_sql('select * from parser_app_category_titles', con=db_connection)
    global_ = Global()

    res = pd.DataFrame(columns=['date', 'type', 'category_id', 'category_title',
                        'site_title', 'price_new', 'price_old', 'site_unit',
                        'site_link', 'site_code'])
    i = 0
    for link in tqdm(urls_vprok):
        i += 1
        time.sleep(np.abs(np.random.randn())*3)
        if global_.is_tor_vprok:
            print('\nTOR ON')
        vprok_data = vprok.get_data_from_link(link, global_ = global_)
        print(categories_df.loc[categories_df.category_id==URLS.loc[URLS['site_link']==link, 'category_id'].values[0],'category_title'].values[0])
        if vprok_data:
            category_id = URLS.loc[URLS['site_link']==link, 'category_id'].values[0]
            category_title = categories_df.loc[categories_df.category_id==category_id,'category_title'].values[0]
            price_dict = {'date': datetime.datetime.now().date().strftime(r"%Y-%m-%d"),
                            'miss': 0,
                            'type': 'food',
                            'category_id': category_id,
                            'category_title': category_title,
                            'site_title': vprok_data['site_title'],
                            'price_new': vprok_data['price_new'],
                            'price_old': vprok_data['price_old'],
                            'site_unit': vprok_data['site_unit'],
                            'site_link': link,
                            'site_code': 'vprok'}
            print(price_dict)
            print('---------------------')
            one_row_res = pd.DataFrame([price_dict])
            res = pd.concat([res, one_row_res], ignore_index=True)          
              
    res.to_csv('data.csv')
    res.to_sql(name='parser_app_pricesraw', con=db_connection, if_exists='append', index=False)

if __name__ == '__main__':
    main()