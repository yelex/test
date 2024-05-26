import pandas as pd
import sys

print(sys.platform)

HEADERS_VPROK = {
    "Accept": "*/*",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US;q=0.5,en;q=0.3",
    "Cache-Control": "max-age=0",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://google.com",
}

HEADERS_GLOBUS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'Cookie': 'i=AelZhzQvtGw2ryGDaN7JGaz9O02WNtdATOdsKjnnfEGg9R2s7a9NQXNLaN2zclo6EB5+Q/RkPMq+67rWiduW7v/Kwn4=; yandexuid=8190459421711055783; yashr=4313643991711055783; yuidss=8190459421711055783; ymex=2026539258.yrts.1711179258; _ym_uid=1711179263257287820; yandex_gid=213; _ym_d=1711179822; gdpr=0; yandex_login=e-alexey94; Session_id=3:1711796618.5.0.1711181348164:1gryLg:89.1.2:1|734956111.0.2.3:1711181348|3:10285281.590607.khbRxrJkto7PTFeHyFYofZ188B4; sessar=1.1188.CiA4Yke5mIE69BEETs0xudXLfff55akdrHYZXeF1Hw_4Ag.uTfunzh6-fOVWTKyrDSjfbwR9Z-VRCno1WzzM2R-ukw; sessionid2=3:1711796618.5.0.1711181348164:1gryLg:89.1.2:1|734956111.0.2.3:1711181348|3:10285281.590607.fakesign0000000000000000000; bh=EkEiTWljcm9zb2Z0IEVkZ2UiO3Y9IjEyMyIsICJOb3Q6QS1CcmFuZCI7dj0iOCIsICJDaHJvbWl1bSI7dj0iMTIzIhoFIng4NiIiDyIxMjMuMC4yNDIwLjY1IioCPzA6CSJXaW5kb3dzIkIIIjE1LjAuMCJKBCI2NCJSWiJNaWNyb3NvZnQgRWRnZSI7dj0iMTIzLjAuMjQyMC42NSIsIk5vdDpBLUJyYW5kIjt2PSI4LjAuMC4wIiwiQ2hyb21pdW0iO3Y9IjEyMy4wLjYzMTIuODciIg==; is_gdpr=0; is_gdpr_b=CLj5IhDA8wEoAg==; bh=Ej8iTWljcm9zb2Z0IEVkZ2UiO3Y9IjEyMyIsIk5vdDpBLUJyYW5kIjt2PSI4IiwiQ2hyb21pdW0iO3Y9IjEyMyIaBSJ4ODYiIg8iMTIzLjAuMjQyMC42NSIqAj8wOgkiV2luZG93cyJCCCIxNS4wLjAiSgQiNjQiUloiTWljcm9zb2Z0IEVkZ2UiO3Y9IjEyMy4wLjI0MjAuNjUiLCJOb3Q6QS1CcmFuZCI7dj0iOC4wLjAuMCIsIkNocm9taXVtIjt2PSIxMjMuMC42MzEyLjg3IiI=; yp=2027163988.pcs.1#4294967295.skin.s#1713771815.ygu.1#2026541348.udn.cDplLWFsZXhleTk0#1712401917.szm.1%3A2560x1440%3A1270x1308; yabs-sid=1797179211712476995',
    'Origin': 'https://online.globus.ru',
    'Referer': 'https://online.globus.ru/',
    'Sec-Ch-Ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'

}

TIMEOUT = 120
URLS = pd.read_csv(r"./links/final_links.csv", index_col=0, sep=";")

DB_CONNECTION_STR = (
    "mysql+pymysql://root:password@localhost/ane_base"
)

PIECE_UNITS = ["шт", "штук", "штуки", "штука", "пак", "пакетиков", "пак"]
KG_UNITS = ["кг", "kg", "килограмм"]  # оставить в граммах
GRAM_UNITS = ["г", "g", "грамм", "граммов", "гр"]  # в кг
LITRE_UNITS = ["л", "l", "литр", "литров", "литра"]
ML_UNITS = ["мл", "ml", "миллилитров", "миллилитра"]
TENPIECE_UNITS = ["10 шт", "10 шт.", "10шт", "10шт.", "десяток", "дес."]


TOKEN = "6652904233:AAEA5YF9-eed_7juox6hGm6fxLgkJBbxHMc"
LOG_CHANNEL = "-2117830128"


PATH_CHROMEDRIVER = "./chromedrivers/chromedriver.exe" if sys.platform=='win32' else '/usr/lib/chromium-browser/chromedriver'
