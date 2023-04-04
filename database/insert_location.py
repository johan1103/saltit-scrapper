import pymysql.cursors
import pandas as pd
import time
import properties


def get_locations_by_tuple(city_name, location_dict):
    locations = []
    data = pd.read_csv('../static/summary/restaurant-summary-' + city_name + '.csv')
    raw_dict = data.to_dict('index')
    for idx, raw_value in raw_dict.items():
        is_duplicated = location_dict.get(raw_value['rid'], 'NO_KEY')
        if is_duplicated != 'NO_KEY':
            continue
        location_dict[raw_value['rid']] = {'name': raw_value['name']}
        locations.append({'rid': raw_value['rid'], 'latitude': raw_value['lat'], 'longitude': raw_value['lng'],
                          'road_address': raw_value['address']})

    return locations


def get_restaurant_id_by_dict(curs):
    dicts = {}
    sql = "select * from restaurant"
    curs.execute(sql)
    result = curs.fetchall()
    for data in result:
        dicts[data[4]] = {'id': data[0]}
    return dicts


def insert_db(curs, list):
    datas = []
    for res in list:
        datas.append([res['restaurant_id'], res['latitude'], res['longitude'], res['road_address']])
    query = "insert into restaurant_location(restaurant_id,latitude,longitude,road_address) " \
            "values (%s, %s, %s, %s);"
    curs.executemany(query, datas)


if __name__ == '__main__':
    conn = properties.get_db_properties()
    cities = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', '서울', '세종', '울산', '인천', '전남', '전북',
              '제주', '충남', '충북']
    start = time.time()
    locations_dict = {}
    curs = conn.cursor()
    restaurant_id_dict = get_restaurant_id_by_dict(curs)
    for city_name in cities:
        print(city_name)
        location_list = get_locations_by_tuple(city_name, locations_dict)
        for location in location_list:
            rid = location['rid']
            restaurant_id = restaurant_id_dict[rid]['id']
            location['restaurant_id'] = restaurant_id
        insert_db(curs, location_list)
        conn.commit()
    conn.close()
    print("location insert time :", time.time() - start)
