import pandas as pd
from save_file import save_as_excel
import re


def get_restaurants_by_list(city_name):
    data = pd.read_csv('../static/menu/menu-' + city_name + '.csv')
    menus = data.to_dict('records')
    return menus


def change_price_to_int(menus):
    for menu in menus:
        price_str = menu['price']
        if type(price_str) != str:
            continue
        only_number_str = re.sub(r'[^0-9]', '', price_str)
        can_convert_to_int = re.match(r'[0-9]', only_number_str)
        if can_convert_to_int is None:
            continue
        price_int = int(only_number_str)
        menu['price'] = price_int
        print(price_int)
    return


if __name__ == '__main__':
    menu_list = get_restaurants_by_list('서울')
    change_price_to_int(menu_list)
    save_as_excel(menu_list, '서울')
