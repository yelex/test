import pandas as pd

HEADERS = {'Accept': '*/*', 
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36', 
           'Accept-Encoding': 'gzip, deflate, br', 
           'Accept-Language': 'en-US;q=0.5,en;q=0.3', 'Cache-Control': 'max-age=0', 
           'DNT': '1', 'Upgrade-Insecure-Requests': '1', 'Referer': 'https://google.com'}

TIMEOUT = 120
URLS = pd.read_csv(r'./links/final_links.csv', index_col=0, sep=';')