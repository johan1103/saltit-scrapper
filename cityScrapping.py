import json
import requests


def scrapping_city():
    cities = []
    data = {'mode': 'district'}
    url = 'https://im.diningcode.com/API/isearch/'
    chrome_header = {
        'Accept': 'application/json, text/plain, */*',
        'Host': 'im.diningcode.com',
        'Origin': 'https://www.diningcode.com',
        'Referer': 'https://www.diningcode.com/',
        'User-Agent': 'Mozilla/5.0'
    }
    res = requests.post(url=url, headers=chrome_header, data=data)
    res_dict = json.loads(res.text)
    city_dict = res_dict['result_data']['district']
    for city in city_dict:
        # 서울
        first_city_name = city['name']
        print(city)
        for child_name in city['child']:
            # 강남구
            print(first_city_name)
            second_city_name = child_name['name']
            for grand_child_name in child_name['child']:
                # 강남역, 압구정....
                city_name = first_city_name + ' ' + second_city_name + ' ' + grand_child_name
                cities.append(city_name)
    return cities


if __name__ == '__main__':
    result_cities = scrapping_city()
    f = open("static/cities.txt", 'w')
    for name in result_cities:
        f.write('city name : ')
        f.write(name)
        f.write('\n')
        print(name)
    f.close()