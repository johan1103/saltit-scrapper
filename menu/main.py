import time

import pandas as pd
from menu_scrapping import scrapping_menus
from save_file import save_as_excel


def get_restaurants_by_dict(city_name):
    data = pd.read_csv('../static/summary/restaurant-summary-' + city_name + '.csv')
    raw_dict = data.to_dict('index')
    convert_dict = {}
    for idx, raw_value in raw_dict.items():
        convert_dict[raw_value['rid']] = {'rid': raw_value['rid'], 'name': raw_value['name'],
                                          'address': raw_value['address']}
    return convert_dict


if __name__ == '__main__':
    cities = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', '서울', '세종', '울산', '인천', '전남', '전북',
              '제주', '충남', '충북']
    for name in cities:
        start = time.time()
        # 테스트 용도로 서울의 식당 데이터 20개만 추출
        if name == '서울':
            restaurants = get_restaurants_by_dict(city_name=name)
            menus = scrapping_menus(restaurants)
            save_as_excel(menus, name)
            f = open(f"../static/summary/scrapping_time_{name}.txt", 'w')
            f.write(f'{name} scrapping time : ')
            f.write(str(time.time() - start))
            f.close()
