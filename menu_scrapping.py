import pandas as pd


def get_restaurants_by_dict(city_name):
    data = pd.read_csv('static/restaurant-summary-' + city_name + '.csv')
    raw_dict = data.to_dict('index')
    convert_dict = {}
    cnt = 0
    for idx, raw_value in raw_dict.items():
        cnt += 1
        convert_dict[raw_value['rid']] = {'rid': raw_value['rid'], 'name': raw_value['name'],
                                          'address': raw_value['address']}
        # 기능 테스트 용도로 식당 데이터 20개만 추출
        if cnt > 20:
            break
    return convert_dict


if __name__ == '__main__':
    cities = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', '서울', '세종', '울산', '인천', '전남', '전북',
              '제주', '충남', '충북']
    url = 'https://www.diningcode.com/profile.php?rid='
    chrome_header = {
        'Accept': 'application/json, text/plain, */*',
        'Host': 'im.diningcode.com',
        'Origin': 'https://www.diningcode.com',
        'Referer': 'https://www.diningcode.com/',
        'User-Agent': 'Mozilla/5.0'
    }
    for name in cities:
        # 테스트 용도로 서울의 식당 데이터 20개만 추출
        if name == '서울':
            restaurants = get_restaurants_by_dict(city_name=name)
