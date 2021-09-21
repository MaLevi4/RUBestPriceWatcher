import requests
import json
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_mvideo_price(url):
    cookies = {'MVID_TIMEZONE_OFFSET': "3", 'MVID_CITY_ID': "CityCZ_975", 'MVID_REGION_SHOP': "S002",
               'bIPs': "-1341531712",
               'MVID_REGION_ID': "1", 'JSESSIONID': "rxQShFNJp0jbbdQw81Q2F1bDTMfJPq6YXJQTLdcgRJQypDLmMFMV!-1352658948"}
    response = requests.get(url, headers={'User-Agent': 'My User Agent 1.0'}, cookies=cookies)
    if response.status_code == 200:
        content = json.loads(response.text)
        return content['body']['materialPrices'][0]['price']['salePrice']


def get_biggeek_price(url):
    response = requests.get(url, headers={'User-Agent': 'My User Agent 1.0'}, verify=False)
    if response.status_code == 200:
        matches_list = re.findall(
            r'<div class=\"product-price\">\s+<span class=\"price-value\">(\d+\s?\d*)</span>', response.text)
        return int(matches_list[0].replace(' ', ''))


def get_restore_price(url):
    response = requests.get(url, headers={'User-Agent': 'My User Agent 1.0'}, verify=False)
    if response.status_code == 200:
        matches_list = re.findall(r'\"unitSalePrice\":(\d+),', response.text)
        return int(matches_list[0])


def get_eldorado_price(url):
    response = requests.get(url, headers={'User-Agent': 'My User Agent 1.0'}, verify=False)
    if response.status_code == 200:
        matches_list = re.findall(r',\"price\":\"(\d+)\",', response.text)
        return int(matches_list[0])


def get_citilink_price(url):
    response = requests.get(url, headers={'User-Agent': 'My User Agent 1.0'}, verify=False)
    if response.status_code == 200:
        matches_list = re.findall(r'\"price\":\s\"(\d+)\",', response.text)
        return int(matches_list[0])


def get_ozon_price(url):
    response = requests.get(url, headers={'User-Agent': 'My User Agent 1.0'}, verify=False)
    if response.status_code == 200:
        matches_list = re.findall(r',\"price\":\"(\d+)\",', response.text)
        return int(matches_list[0])


def get_yamarket_price(url):
    return -1


def get_dns_price(url):
    return -1


shops = {'M Video': {'func': get_mvideo_price, 'urls': ("https://www.mvideo.ru/bff/products/prices?productIds=30043367&isPromoApplied=true&addBonusRubles=true&isPricingEngineFinalPrice=true", "https://www.mvideo.ru/bff/products/prices?productIds=30043368&isPromoApplied=true&addBonusRubles=true&isPricingEngineFinalPrice=true", "https://www.mvideo.ru/bff/products/prices?productIds=30043366&isPromoApplied=true&addBonusRubles=true&isPricingEngineFinalPrice=true")},
         'BigGeek': {'func': get_biggeek_price, 'urls': ("https://biggeek.ru/products/apple-ipad-mini-2019-256gb-wi-fi-sellular-space-gray", "https://biggeek.ru/products/apple-ipad-mini-2019-256gb-wi-fi-sellular-silver", "https://biggeek.ru/products/apple-ipad-mini-2019-256gb-wi-fi-sellular-gold")},
         'Re Store': {'func': get_restore_price, 'urls': ("https://re-store.ru/catalog/MUXD2RU-A/", "https://re-store.ru/catalog/MUXE2RU-A/", "https://re-store.ru/catalog/MUXC2RU-A/")},
         'Eldorado': {'func': get_eldorado_price, 'urls': ("https://www.eldorado.ru/cat/detail/planshet-apple-ipad-mini-7-9-wi-fi-plus-cellular-256gb-space-gray-muxc2ru-a/", "https://www.eldorado.ru/cat/detail/planshet-apple-ipad-mini-7-9-wi-fi-cellular-256gb-silver-muxd2ru-a/", "https://www.eldorado.ru/cat/detail/planshet-apple-ipad-mini-7-9-wi-fi-cellular-256gb-gold-muxe2ru-a/")},
         'Citilink': {'func': get_citilink_price, 'urls': ("https://www.citilink.ru/product/planshet-apple-ipad-mini-2019-256gb-wi-fi-cellular-muxe2ru-a-2gb-256gb-1138921/", "https://www.citilink.ru/product/planshet-apple-ipad-mini-2019-256gb-wi-fi-cellular-muxd2ru-a-2gb-256gb-1138918/")},
         'Ozon': {'func': get_ozon_price, 'urls': ("https://www.ozon.ru/product/7-9-planshet-apple-ipad-mini-wi-fi-cellular-2019-256-gb-serebristyy-150631297/?sh=9sVsgP7N",)},
         'Yandex Market': {'func': get_yamarket_price, 'urls': ("https://market.yandex.ru/product--planshet-apple-ipad-mini-2019-256gb-wi-fi-cellular/415565465?cpa=1&sku=100607013387&glfilter=14871214%3A14896128_100607013387", "https://market.yandex.ru/product--planshet-apple-ipad-mini-2019-256gb-wi-fi-cellular/415565465?cpa=1&sku=100607013385&glfilter=14871214%3A14897983_100607013385", "https://market.yandex.ru/product--planshet-apple-ipad-mini-2019-256gb-wi-fi-cellular/415565465?cpa=1&sku=100607013386&glfilter=14871214%3A15324855_100607013386")},
         'DNS': {'func': get_dns_price, 'urls': ("https://www.dns-shop.ru/product/5c2a675a4c563332/79-planset-apple-ipad-mini-2019-256-gb-3g-lte-zolotistyj/", "https://www.dns-shop.ru/product/398b0ec24c553332/79-planset-apple-ipad-mini-2019-256-gb-3g-lte-seryj/", "https://www.dns-shop.ru/product/23ce62cb4c563332/79-planset-apple-ipad-mini-2019-256-gb-3g-lte-serebristyj/")}}

if __name__ == '__main__':
    min_price = 0
    target_shop = ""

    for shop in shops:
        print(f"--- {shop} ---")
        for url in shops[shop]['urls']:
            price = shops[shop]['func'](url)
            print(price, url)

            if price == -1:
                continue
            if min_price == 0 or price < min_price:
                min_price = price
                target_shop = shop
        print()

    print("===============================")
    print(f"Min price is {min_price} rub in {target_shop}")
