import requests
from bs4 import BeautifulSoup


def find_menu_block(soup):
    try:
        menu_block = soup.find(class_='Restaurant_MenuList')
    except AttributeError as e:
        return None
    return menu_block

def scrapping_menus(restaurants):
    base_url = 'https://www.diningcode.com/profile.php?rid='
    chrome_header = {
        'Accept': 'text/html, */*',
        'User-Agent': 'Mozilla/5.0'
    }
    restaurant_menus = []
    for rid, restaurant in restaurants.items():
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
            price = li_block.find(class_='Restaurant_MenuPrice')
            restaurant_menus.append({'address': restaurant['address'], 'rid': rid, 'name': name.text,
                                     'price': price.text, 'order_number': order_number})

        print(restaurant_menus)
        break

