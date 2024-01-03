import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import re
import time


options = uc.ChromeOptions()
# options.add_argument("--headless");
options.add_argument("--no-sandbox");
options.add_argument("--disable-dev-shm-usage");
options.add_argument("--disable-browser-side-navigation");
options.add_argument("--disable-gpu");
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument("--enable-javascript")
driver = uc.Chrome(options=options)

driver.get("https://www.vprok.ru/")

# print(BeautifulSoup(driver.page_source, 'html.parser').text)
time.sleep(3)

# cookies = [
#             {'domain': 'www.vprok.ru', 'expiry': 1702987373, 'httpOnly': False, 'name': '_POBP_s',
#              'path': '/',
#              'sameSite': 'Strict', 'secure': False,
#              'value': 'rum=1&id=9ff77df3-8740-4498-a0b5-4b9f2a57aefc&created=1702986445896&expire=1702987345897'},
#             {'domain': 'www.vprok.ru', 'expiry': 1703072849, 'httpOnly': False, 'name': 'tmr_detect',
#              'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': '0%7C1702986449988'},
#             {'domain': '.vprok.ru', 'expiry': 1703029648, 'httpOnly': False, 'name': 'adrdel', 'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': '1'},
#             {'domain': '.vprok.ru', 'expiry': 1737546447, 'httpOnly': False, 'name': '_ga', 'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': 'GA1.2.1966389030.1702986447'},
#             {'domain': '.vprok.ru', 'expiry': 1737546447, 'httpOnly': False, 'name': 'mindboxDeviceUUID',
#              'path': '/', 'sameSite': 'Lax', 'secure': False,
#              'value': 'ce04ce07-33f8-4bc7-8ad2-bba7a857f294'},
#             {'domain': 'www.vprok.ru', 'expiry': 1737546447, 'httpOnly': False, 'name': '_sp_id.509b',
#              'path': '/',
#              'sameSite': 'None', 'secure': True,
#              'value': 'a54abe4b-0305-4f64-a611-df6271443379.1702986447.1.1702986447..a8667b9b-b544-4a30-b30c-5160ac06095e..7339305b-5f92-4405-8fe1-d2c0a6e3f54a.1702986447357.6'},
#             {'domain': '.vprok.ru', 'expiry': 1734522447, 'httpOnly': False, 'name': '_ym_d', 'path': '/',
#              'sameSite': 'None', 'secure': True, 'value': '1702986447'},
#             {'domain': '.vprok.ru', 'expiry': 1734522447, 'httpOnly': False, 'name': '_ym_uid', 'path': '/',
#              'sameSite': 'None', 'secure': True, 'value': '1702986447556884953'},
#             {'domain': '.vprok.ru', 'expiry': 1702986506, 'httpOnly': False, 'name': '_gat_UA-93122031-1',
#              'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'},
#             {'domain': '.vprok.ru', 'expiry': 1737546448, 'httpOnly': False, 'name': 'adrcid', 'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': 'AiygCdTW_gQl4TLPFG29T2w'},
#             {'domain': '.vprok.ru', 'expiry': 1731757646, 'httpOnly': False, 'name': 'tmr_lvidTS',
#              'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': '1702986446828'},
#             {'domain': '.vprok.ru', 'expiry': 1702988247, 'httpOnly': False, 'name': '_ym_visorc',
#              'path': '/',
#              'sameSite': 'None', 'secure': True, 'value': 'w'},
#             {'domain': '.vprok.ru', 'expiry': 1703072847, 'httpOnly': False, 'name': '_gid', 'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': 'GA1.2.553670366.1702986447'},
#             {'domain': 'www.vprok.ru', 'expiry': 1702988247, 'httpOnly': False, 'name': '_sp_ses.509b',
#              'path': '/',
#              'sameSite': 'None', 'secure': True, 'value': '*'},
#             {'domain': '.vprok.ru', 'expiry': 1703058447, 'httpOnly': False, 'name': '_ym_isad',
#              'path': '/',
#              'sameSite': 'None', 'secure': True, 'value': '2'},
#             {'domain': '.vprok.ru', 'expiry': 1737546446, 'httpOnly': False, 'name': 'iap.uid', 'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': 'a14609fe0adf43d38b9166afe5a22627'},
#             {'domain': 'www.vprok.ru', 'expiry': 1737546446, 'httpOnly': False, 'name': 'slsession',
#              'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': '6EDECAD2-64A6-448D-B926-D0649F019E01'},
#             {'domain': '.vprok.ru', 'httpOnly': True, 'name': 'aid', 'path': '/', 'sameSite': 'Lax',
#              'secure': True,
#              'value': 'eyJpdiI6IjEyV2NUN1dnVVp3VmczbE5RdUViXC9BPT0iLCJ2YWx1ZSI6IlU4cGdyc256VjVNTTJtbHUyQTVTV09GMWFVbUxzTlpsT0M3K1J5dTR6N0x2TVArUUV5T3lRS0dcL1Q0Q1ZWV3gyV3VpbU0xWHViczFad0ZxS1l3S2dqZz09IiwibWFjIjoiNDE2OTU0YmUzNTIzYWQ1YTk1Y2RmNWEzMGFiNmU5MGY2OGVlNTg5NTg4Y2U4OTEzYjkyNzRjNjhhMzA0Nzk5MSJ9'},
#             {'domain': '.vprok.ru', 'expiry': 1737546445, 'httpOnly': False, 'name': 'standardShopId',
#              'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': '2527'},
#             {'domain': '.vprok.ru', 'expiry': 1702987645, 'httpOnly': False, 'name': 'XSRF-TOKEN',
#              'path': '/',
#              'sameSite': 'Lax', 'secure': True,
#              'value': 'eyJpdiI6IndHNnlcL3RuZ0xqcWVONnhEUTQrQXBnPT0iLCJ2YWx1ZSI6InFCSjhMTldqU0k3ZkZVMCtaTjVkV2tNckg3XC9JZG5LbWVnRVBvd3dDQWlpMmQ0bjllY3hHb0MxS1JEYUx6NkhoTG0xMkdiTzFVVVJkYTRTaHpZd2JVQT09IiwibWFjIjoiYTJmZGI2MzU4OTY1NDcwNjM0M2E0MTM3YTk4Zjg1ZDMzZjZkODhkOTMyZmRhNGI4ZDM2MzNkYmFiMjFiMjMyNSJ9'},
#             {'domain': '.vprok.ru', 'expiry': 1731757646, 'httpOnly': False, 'name': 'tmr_lvid',
#              'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': 'd09060c13954cdc63cf0d5fa4d6fdb4a'},
#             {'domain': '.vprok.ru', 'httpOnly': False, 'name': 'suuid', 'path': '/', 'sameSite': 'Lax',
#              'secure': False, 'value': '83fa72a0-8930-460e-944b-4477b268e424'},
#             {'domain': 'www.vprok.ru', 'expiry': 1737546446, 'httpOnly': False, 'name': 'slid', 'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': '658182ced86afccf47076745'},
#             {'domain': '.vprok.ru', 'expiry': 1737546445, 'httpOnly': False, 'name': 'deliveryTypeId',
#              'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': '1'},
#             {'domain': '.vprok.ru', 'expiry': 1737546447, 'httpOnly': False, 'name': 'directCrm-session',
#              'path': '/', 'sameSite': 'Lax', 'secure': False,
#              'value': '%7B%22deviceGuid%22%3A%22ce04ce07-33f8-4bc7-8ad2-bba7a857f294%22%7D'},
#             {'domain': '.vprok.ru', 'expiry': 1737546445, 'httpOnly': False, 'name': 'region', 'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': '1'},
#             {'domain': '.vprok.ru', 'expiry': 1737546447, 'httpOnly': False, 'name': '_ga_GK2L3NTRC5',
#              'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': 'GS1.1.1702986447.1.0.1702986447.60.0.0'},
#             {'domain': '.vprok.ru', 'expiry': 1737546445, 'httpOnly': False, 'name': 'split_segment_amount',
#              'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '11'},
#             {'domain': '.vprok.ru', 'expiry': 1734608845, 'httpOnly': False, 'name': 'luuid', 'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': 'b2f77a38-049d-4cd1-ba09-90996af9d824'},
#             {'domain': '.vprok.ru', 'expiry': 1737546445, 'httpOnly': False, 'name': 'split_segment',
#              'path': '/',
#              'sameSite': 'Lax', 'secure': False, 'value': '0'},
#             {'domain': 'www.vprok.ru', 'expiry': 1731757647, 'httpOnly': False, 'name': 'flocktory-uuid',
#              'path': '/', 'sameSite': 'Lax', 'secure': False,
#              'value': '8d587b69-c181-4983-8601-eb66bbdac654-5'},
#             {'domain': '.vprok.ru', 'expiry': 1737546445, 'httpOnly': True, 'name': 'access_token',
#              'path': '/',
#              'sameSite': 'Lax', 'secure': False,
#              'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5IiwianRpIjoidXVpZGIyZjc3YTM4LTA0OWQtNGNkMS1iYTA5LTkwOTk2YWY5ZDgyNDU3MDFkZjhiMWIyNmY1MjcwMWM1NDMzNjkyMmY3NzNjNmM2ZmE2YjIiLCJpYXQiOjE3MDI5ODY0NDUuMjY4MDA1LCJuYmYiOjE3MDI5ODY0NDUuMjY4MDA3LCJleHAiOjE3MDI5ODgyNDUuMjY0MDAxLCJzdWIiOiIiLCJzY29wZXMiOltdLCJzcGxpdF9zZWdtZW50IjowLCJ4NWlkX2FjY2Vzc190b2tlbiI6IiIsImN1c3RvbWVyX3V1aWQiOiIifQ.mjAXoDUgb3295y2WVqYwIOh1BtaEZwaGYmIIsrB6QLW77C45-0d-jMAxvFRFw2Js-gODfKxLP20fsuYcDCrH3gBqqbgX5FI2S_fgD03G2w-lW2LfKnOfWHcep4D2StnDepcj9PUn8fFXf82JXZv2F90H9vGvS-grbT12CvVEpKL6NNJrlIJLlV09eJR0ZwbK5nvxuVw7DTxYlrmBH1An_2kDaWrBtdWkcAJMmXw9qQECxunSBDQ6oxTEbgHt_2v8BjZhJsrQBW9tRIw4RL2wrejMDpVzzFJJR5t96yEBzzBRYquVkiWKrHs2ZqSIEqcrxegoMS4s98hdEIlSXjRSaCCt6kI04XdNpgN5VhQnIAGph_Q3g1mixx5Y6MQvsFhd9v5x-82JytUq-MU1Yj5V1sULWjJPLGBnxK6fNAS1ZcuaU0_M8ky4nfPI8CIHEk0frU7bfaGdUFKAKZFoCwhYM1pH_f1TlE7JH2VKGuCfLe7eGJuXude5CpGuKSF_rU7nNAeS78uijc0U2Gk2NTGv_NmBAopo43ojoFEgIpALNA72UxY4heoQx1THwTJnnhvdty2gGnsi1EVn3j5mdOXBe83grYTm4YjSnRzgQT5NRiW3ymgxqA0geVD6htwtZPFr7HmSN_9spUAWCR-rBieqKTqO0pDVZwti6ZMrAx8iFWo'},
#             {'domain': '.www.vprok.ru', 'expiry': 1703072840, 'httpOnly': False,
#              'name': 'ngenix_jscv_a68b51100641',
#              'path': '/', 'sameSite': 'Lax', 'secure': False,
#              'value': 'payload=GbkD7NDenv64%2Fzik9c4XtM4FkmteO2HnF09jFrhG3Z1rK9%2FEbxUU8l1ldK1GBZ84&session_id_e0227498=590e5448675761c8d719decfee58f066&cookie_signature=arNXRQUIRZlYNYuX38C9vPK3Dn0%3D&challenge_complexity=10&visitor_id_af50ddc3=4bff40792c903e83d21ca37cdf262920&bot_profile_check=true&cookie_expires=1703072840'}]
# for cookie in cookies:
# 	driver.add_cookie(cookie)
driver.get("https://www.vprok.ru/product/miratorg-mirat-steyk-iz-sheyk-sv-gzms400g--393530")
time.sleep(10)
soup = BeautifulSoup(driver.page_source, 'lxml')

print(soup.text)
print(soup.find('h1', {'class': re.compile('Title_title__nvodu')}).text)
driver.close()
