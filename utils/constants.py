import pandas as pd
import sys
print(sys.platform)

HEADERS_VPROK = {'Accept': '*/*', 
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36', 
           'Accept-Encoding': 'gzip, deflate, br', 
           'Accept-Language': 'en-US;q=0.5,en;q=0.3', 'Cache-Control': 'max-age=0', 
           'DNT': '1', 'Upgrade-Insecure-Requests': '1', 'Referer': 'https://google.com'}

HEADERS_GLOBUS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15'}


TIMEOUT = 120
URLS = pd.read_csv(r'./links/final_links.csv', 
                   index_col=0, sep=';')

DB_CONNECTION_STR = 'mysql+pymysql://root:Fokina12@localhost/ane_base' if sys.platform != 'linux' else 'mysql+pymysql://root:password@localhost/ane_base'

PIECE_UNITS = ['шт', 'штук', 'штуки', 'штука', 'пак', 'пакетиков', 'пак']
KG_UNITS = ['кг', 'kg', 'килограмм']  # оставить в граммах
GRAM_UNITS = ['г', 'g', 'грамм', 'граммов', 'гр']  # в кг
LITRE_UNITS = ['л', 'l', 'литр', 'литров', 'литра']
ML_UNITS = ['мл', 'ml', 'миллилитров', 'миллилитра']
TENPIECE_UNITS = ['10 шт', '10 шт.', '10шт', '10шт.', 'десяток', 'дес.']
