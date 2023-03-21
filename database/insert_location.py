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


def get_locations_by_tuple(city_name, locations):
    data = pd.read_csv('../static/summary/restaurant-summary-' + city_name + '.csv')
    raw_dict = data.to_dict('index')
    for idx, raw_value in raw_dict.items():
        locations.append({'rid': raw_value['rid'], 'latitude': raw_value['lat'], 'longitude': raw_value['lng'],
                          'road_address': raw_value['address']})
    return


def get_restaurant_id_by_dict(curs):
    dicts = {}
    sql = "select * from restaurant"
    curs.execute(sql)
    result = curs.fetchall()
    for data in result:
        dicts[data[3]] = {'id': data[0]}
    return dicts


def insert_db(curs, list):
    datas = []
    now = datetime.now()
    for res in list:
        datas.append([res['restaurant_id'], res['latitude'], res['longitude'], res['road_address']])
    query = "insert into restaurant_location(restaurant_id,latitude,longitude,road_address) " \
            "values (%s, %s, %s, %s);"
    curs.executemany(query, datas)


if __name__ == '__main__':
    cities = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', '서울', '세종', '울산', '인천', '전남', '전북',
              '제주', '충남', '충북']
    curs = conn.cursor()
    restaurant_id_dict = get_restaurant_id_by_dict(curs)
    for city_name in cities:
        if city_name != '서울':
            continue
        location_list = []
        get_locations_by_tuple(location_list)
        for location in location_list:
            rid = location['rid']
            restaurant_id = restaurant_id_dict[rid]['id']
            location['restaurant_id'] = restaurant_id
        insert_db(curs, location_list)
