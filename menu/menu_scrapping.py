import requests
import re
import time
from random import random
from bs4 import BeautifulSoup


def find_menu_block(soup):
    try:
        menu_block = soup.find(class_='Restaurant_MenuList')
    except AttributeError as e:
        return None
    return menu_block


def change_price_to_int(price_str):
    only_number_str = re.sub(r'[^0-9]', '', price_str)
    can_convert_to_int = re.match(r'[0-9]', only_number_str)
    if can_convert_to_int is None:
        return ''
    price_int = int(only_number_str)
    return price_int


def scrapping_menus(restaurants):
    time.sleep(random()/5)
    base_url = 'https://www.diningcode.com/profile.php?rid='
    chrome_header = {
        'Accept': 'text/html, */*',
        'User-Agent': 'Mozilla/5.0'
    }
    restaurant_menus = []
    for rid, restaurant in restaurants.items():
        print(restaurant['address'] + ',' + restaurant['name'])
        url = base_url + rid
        page = requests.get(url=url, headers=chrome_header)
        soup = BeautifulSoup(page.text, "html.parser")
        menu_block = find_menu_block(soup)
        if menu_block is None:
            continue
        li_blocks = menu_block.find_all("li")
        order_number = 0
        for li_block in li_blocks:
            order_number += 1
            name = li_block.find(class_='Restaurant_Menu')
            price_block = li_block.find(class_='Restaurant_MenuPrice')
            price_int = change_price_to_int(price_block.text)
            restaurant_menus.append({'address': restaurant['address'], 'rid': rid, 'name': name.text,
                                     'price': price_int, 'order_number': order_number})
    return restaurant_menus

