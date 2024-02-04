import numpy as np
import time
import datetime
import pandas as pd
import sys
import os
from tqdm import tqdm
from sqlalchemy import create_engine
import logging


sys.path.insert(0, os.path.abspath('./'))
from utils.constants import URLS, DB_CONNECTION_STR
from global_state import Global
from scrappers import vprok, globus

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', encoding='UTF-8')

global_ = Global()
urls_vprok = URLS.loc[URLS.site_link.str.contains('vprok'), 'site_link']
urls_globus = URLS.loc[URLS.site_link.str.contains('globus'), 'site_link']

db_connection = create_engine(DB_CONNECTION_STR)
categories_df = pd.read_sql('select * from parser_app_category_titles', con=db_connection)

def get_data(link: str, data: dict, categories_df=categories_df):
    if data:
        category_id = URLS.loc[URLS['site_link']==link, 'category_id'].values[0]
        category_title = categories_df.loc[categories_df.category_id==category_id,'category_title'].values[0]
        site_code = URLS.loc[URLS['site_link']==link, 'site_code'].values[0]
        price_dict = {'date': datetime.datetime.now().date().strftime(r"%Y-%m-%d"),
                        'miss': 0,
                        'type': 'food',
                        'category_id': category_id,
                        'category_title': category_title,
                        'site_title': data['site_title'],
                        'price_new': data['price_new'],
                        'price_old': data['price_old'],
                        'site_unit': data['site_unit'],
                        'site_link': link,
                        'site_code': site_code}
        print(price_dict)
        print('---------------------')
        return pd.DataFrame([price_dict])
    else:
        return pd.DataFrame()
    

def main(to_sql=True):

    res = pd.DataFrame(columns=['date', 'type', 'category_id', 'category_title',
                        'site_title', 'price_new', 'price_old', 'site_unit',
                        'site_link', 'site_code'])

    for link in tqdm(urls_vprok): # test
        time.sleep(np.abs(np.random.randn())*3)
        vprok_data = vprok.get_data_from_link(link, global_ = global_)
        logging.info(vprok_data) if vprok_data else logging.warning(f'{link} отсутствуют данные') 
        one_row_df = get_data(link=link, data=vprok_data)
        res = pd.concat([res, one_row_df], ignore_index=True)         

    for link in tqdm(urls_globus):
        time.sleep(np.abs(np.random.randn())*3)
        globus_data = globus.get_data_from_link(link, global_ = global_)
        logging.info(globus_data) if globus_data else logging.warning(f'{link} отсутствуют данные') 
        one_row_df = get_data(link=link, data=globus_data)
        res = pd.concat([res, one_row_df], ignore_index=True)  
              
    res.to_csv('data.csv')
    if to_sql:
        res.to_sql(name='parser_app_pricesraw', con=db_connection, if_exists='append', index=False)

if __name__ == '__main__':
    try:
        main(to_sql=True)
    except Exception as e:
        logging.error(e)