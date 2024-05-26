from bs4 import BeautifulSoup
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
sys.path.insert(0, os.path.abspath("./"))

from utils.tools import wspex_space
from utils.constants import HEADERS_GLOBUS, TIMEOUT
from globals.global_state import Global
import time
import re

classes = dict()

classes["products_div"] = ["div", "css-1hj20p7 css-146vzrl"]

classes["title"] = ["span", "name"]
classes["price_regular_rub"] = ["div", "css-10fcdyq"]
classes["price_regular_kop"] = ["div", "css-1vx8352"]
classes["price_old_rub"] = ["div", "css-19o902r"]
classes["price_old_kop"] = ["div", "css-1mh8qie"]
classes["site_unit"] = ["div", "css-1im3s12"]
classes["is_avaliable"] = ["div", "h2 item-available-title"]


global_ = Global()


def get_data_from_link(link, global_=global_, headers=HEADERS_GLOBUS, timeout=TIMEOUT):
    """
    Сделать сессию вовне
    Если ошибка - возвращать False, инициировать сессию с тор и возвращать сюда же
    """
    driver = global_.webdriver

    driver.get(link)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    products_div = soup.find(
        classes["products_div"][0], {"class": classes["products_div"][-1]}
    )

    if not products_div:
        print("  Нет товара по ссылке\n")
        return False

    title_div = soup.findAll(classes["title"][0],
                                     {"itemprop": classes["title"][-1]})[-1]
    if not title_div:
        print("  Нет названия\n")
        return False

    # is_avaliable = products_div.find(
    #     classes["is_avaliable"][0], {"class": classes["is_avaliable"][-1]}
    # )["style"]

    # if "none" not in is_avaliable:
    #     print(" Товар временно отсутствует!")
    #     return False

    title = wspex_space(title_div.text)

    price_text_rub_div = products_div.find(
        classes["price_regular_rub"][0], {"class": classes["price_regular_rub"][-1]}
    )
    price_text_kop_div = products_div.find(
        classes["price_regular_kop"][0], {"class": classes["price_regular_kop"][-1]}
    )
    price_text_old_rub_div = products_div.find(
        classes["price_old_rub"][0], {"class": classes["price_old_rub"][-1]}
    )

    price_text_old_kop_div = products_div.find(
        classes["price_old_kop"][0], {"class": classes["price_old_kop"][-1]}
    )

    if not price_text_rub_div or not price_text_kop_div:
        return False

    try:
        price_new = float(price_text_rub_div.text.replace(" ", "")) + 0.01 * int(
            re.search(r'\d+', price_text_kop_div.text).group(0)
        )
    except:
        price_new = float(price_text_rub_div.text.replace("\xa0", "")) + 0.01 * int(
            price_text_kop_div.text
        )

    if price_text_old_rub_div:
        price_old_rub = price_text_old_rub_div.text
        price_old_kop = price_text_old_kop_div.text

        price_old = float(price_old_rub + '.' + price_old_kop)

    else:
        price_old = -1.0
    site_unit = products_div.find(
        classes["site_unit"][0], {"class": classes["site_unit"][-1]}
    ).text.strip()

    return {
        "site_title": title,
        "price_new": price_new,
        "price_old": price_old,
        "site_unit": site_unit,
    }


if __name__ == "__main__":
    # link = 'https://online.globus.ru/products/muka-pshenichnaya-globus-khlebopekarnaya-2-kg/'
    # link = 'https://online.globus.ru/products/svinoy-okorok-svyshe-5-kg-1-upakovka-5-6-kg/'
    link = "https://online.globus.ru/products/govyazhya-noga-na-kosti-1-upakovka-500-950-g/"
    print(get_data_from_link(link))
