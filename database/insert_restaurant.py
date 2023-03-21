import pymysql.cursors
import pandas as pd
from datetime import datetime


# connection 정보
conn = pymysql.connect(
    host='localhost',  # host name
    user='root',  # user name
    password='1234',  # password
    db='saltit_test',  # db name
    charset='utf8'
)


def get_restaurants_by_tuple(city_name, restaurants):
    data = pd.read_csv('../static/summary/restaurant-summary-' + city_name + '.csv')
    raw_dict = data.to_dict('index')
    for idx, raw_value in raw_dict.items():
        restaurants.append({'rid': raw_value['rid'], 'score': raw_value['score'], 'name': raw_value['name'],
                            'img': raw_value['img'], 'food_type': raw_value['food_type']})
    return


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
        datas.append([res['rid'], res['score'], now, res['name'], res['img'], res['food_type_id']])
        if len(res['img']) >= 100:
            print('longer than 100')
    query = "insert into restaurant(rid,score,created_at,name,title_image_url,food_type_id) " \
            "values (%s, %s, %s, %s, %s, %s);"
    curs.executemany(query, datas)



if __name__ == '__main__':
    cities = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', '서울', '세종', '울산', '인천', '전남', '전북',
              '제주', '충남', '충북']
    curs = conn.cursor()
    food_type_dict = get_food_type_id_by_dict(curs)

    for city_name in cities:
        if city_name != '서울':
            continue
        restaurant_list = []
        get_restaurants_by_tuple(city_name, restaurant_list)
        for restaurant in restaurant_list:
            food_type_name = restaurant['food_type']
            restaurant['food_type_id'] = food_type_dict[food_type_name]['id']
        insert_db(curs, restaurant_list)
        curs.exe
        conn.commit()
    conn.close()

