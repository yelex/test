from bs4 import BeautifulSoup
import sys
import os
import re
import pprint
sys.path.insert(0, os.path.abspath("./"))

from utils.tools import wspex_space
from utils.constants import HEADERS_GLOBUS, TIMEOUT
from globals.global_state import Global

classes = dict()

classes["products_div"] = ["div", "css-1hj20p7 css-146vzrl"]

classes["title"] = ["h1", "css-qs82cc"]
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

    if global_.is_tor_globus:
        print(global_.tor_session)
        r = global_.tor_session.get(link, headers=headers, timeout=timeout)
    else:
        print(link + "\n")
        r = global_.request_session.get(link, headers=headers, timeout=timeout)

    soup = BeautifulSoup(r.content, "html.parser")
    print(r.content)
    print(soup)
    products_div = soup.find(
        classes["products_div"][0], {"class": classes["products_div"][-1]}
    )

    if not products_div:
        print("  Нет товара по ссылке\n")
        return False

    title_div = products_div.find(classes["title"][0], {"class": classes["title"][-1]})
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
        price_new = int(price_text_rub_div.text.replace(" ", "")) + 0.01 * int(
            price_text_kop_div.text
        )
    except:
        price_new = int(price_text_rub_div.text.replace("\xa0", "")) + 0.01 * int(
            price_text_kop_div.text
        )

    if price_text_old_rub_div:
        price_old_rub = price_text_old_rub_div.text
        price_old_kop = price_text_old_kop_div.text

        price_old = int(price_old_rub + '.' + price_old_kop)

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
    link = "https://online.globus.ru/products/kotlety-kurinye-petruxa-master-domashnie-s-gribami-i-syrom-450-g-729995_ST"
    print(get_data_from_link(link))
