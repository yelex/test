



  # this call executes the js in the page
from bs4 import BeautifulSoup

from fake_useragent import UserAgent
from requests_html import HTMLSession
import time
session = HTMLSession()
ua = UserAgent()

headers={"User-Agent": ua.chrome}

r = session.get('https://www.vprok.ru/product/grushi-konferens-1kg--303700', headers=headers)

r.html.render()
time.sleep(15)
r.html.render()

print(r.html.find('h1')[0].text)
# soup = BeautifulSoup(r.content)
# print(soup)
# print(soup.find('h1', {'class': 'Title_title__nvodu Title_titleBig__AnZT4'}).text)
# print(soup.find('span', {'class': 'Price_price__QzA8L Price_size_XL__MHvC1 Price_role_discount__l_tpE'}).text)
# print(soup.find('span', {'class': 'Price_price__QzA8L Price_size_XS__ESEhJ Price_role_old__r1uT1'}).text)
