import pandas as pd
import time
from datetime import datetime
import configparser as parser
import properties


def get_restaurants_by_tuple(city_name, restaurant_dict):
    restaurants = []
    data = pd.read_csv('../static/summary/restaurant-summary-' + city_name + '.csv')
    data = data.where((pd.notnull(data)), None)
    raw_dict = data.to_dict('index')
    for idx, raw_value in raw_dict.items():
        is_duplicated = restaurant_dict.get(raw_value['rid'], 'NO_KEY')
        if is_duplicated != 'NO_KEY':
            continue
        restaurant_dict[raw_value['rid']] = {'name': raw_value['name']}
        restaurants.append({'rid': raw_value['rid'], 'score': raw_value['score'], 'name': raw_value['name'],
                            'img': raw_value['img'], 'food_type': raw_value['food_type'], 'phone': raw_value['phone']})
    return restaurants


def get_food_type_id_by_dict(curs):
    dicts = {}
    sql = "select * from food_type"
    curs.execute(sql)
    result = curs.fetchall()
    for data in result:
        dicts[data[1]] = {'id': data[0]}
    return dicts


def insert_db(curs, list):
    datas = []
    now = datetime.now()
    for res in list:
        datas.append([res['rid'], res['score'], now, res['name'], res['img'], res['food_type_id'], res['phone']])
    query = "insert into restaurant(rid,score,created_at,name,title_image_url,food_type_id,phone) " \
            "values (%s, %s, %s, %s, %s, %s, %s);"
    curs.executemany(query, datas)


if __name__ == '__main__':
    conn = properties.get_db_properties()
    cities = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', '서울', '세종', '울산', '인천', '전남', '전북',
              '제주', '충남', '충북']
    curs = conn.cursor()
    food_type_dict = get_food_type_id_by_dict(curs)
    start = time.time()
    restaurants_dict = {}
    for city_name in cities:
        print(city_name)
        restaurant_list = get_restaurants_by_tuple(city_name, restaurants_dict)
        for restaurant in restaurant_list:
            food_type_name = restaurant['food_type']
            restaurant['food_type_id'] = food_type_dict[food_type_name]['id']
        insert_db(curs, restaurant_list)
        conn.commit()
    conn.close()
    print("restaurant insert time :", time.time() - start)

