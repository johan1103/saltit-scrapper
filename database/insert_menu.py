import pymysql.cursors
from insert_location import get_restaurant_id_by_dict
import pandas as pd
import re
import time

# connection 정보
conn = pymysql.connect(
    host='localhost',  # host name
    user='root',  # user name
    password='1234',  # password
    db='saltit_test',  # db name
    charset='utf8'
)


def get_menus_by_tuple(city_name, restaurant_menu_dict):
    menus = []
    data = pd.read_csv('../static/menu/menu-' + city_name + '.csv')
    data = data.where((pd.notnull(data)), None)
    raw_dict = data.to_dict('index')
    for idx, raw_value in raw_dict.items():
        menu_key = raw_value['rid'] + str(raw_value['order_number'])
        is_duplicated = restaurant_menu_dict.get(menu_key, 'NO_KEY')
        if is_duplicated != 'NO_KEY':
            continue
        restaurant_menu_dict[menu_key] = {'name': raw_value['name']}
        menus.append({'rid': raw_value['rid'], 'name': raw_value['name'], 'price': raw_value['price'],
                      'order_number': raw_value['order_number']})
    return menus


def insert_db(curs, list):
    max_menu_price = 1000000
    datas = []
    for res in list:
        try:
            res['price'] = int(res['price'])
        except:
            continue
        if res['price'] > max_menu_price:
            continue
        res['name'] = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z()&,+/~_一-鿕㐀-䶵豈-龎\s]", "", res['name'])
        datas.append([res['name'], res['order_number'], res['price'], res['restaurant_id']])
    query = "insert into restaurant_menu(name,order_number,price,restaurant_id) " \
            "values (%s, %s, %s, %s);"
    curs.executemany(query, datas)


if __name__ == '__main__':
    cities = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', '서울', '세종', '울산', '인천', '전남', '전북',
              '제주', '충남', '충북']
    start = time.time()
    duplicated_dict = {}
    curs = conn.cursor()
    restaurant_id_dict = get_restaurant_id_by_dict(curs)
    for city_name in cities:
        print(city_name)
        menu_list = get_menus_by_tuple(city_name, duplicated_dict)
        for menu in menu_list:
            rid = menu['rid']
            restaurant_id = restaurant_id_dict[rid]['id']
            menu['restaurant_id'] = restaurant_id
        insert_db(curs, menu_list)
        conn.commit()
    conn.close()
    print("restaurant insert time :", time.time() - start)
