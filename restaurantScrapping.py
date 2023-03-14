import time
import requests
import json
from random import random


def scrapping_restaurants(restaurants, duplicated_restaurants, city_name):
    data = {'query': city_name, 'from': 0, 'size': 20}
    url = 'https://im.diningcode.com/API/isearch/'
    chrome_header = {
        'Accept': 'application/json, text/plain, */*',
        'Host': 'im.diningcode.com',
        'Origin': 'https://www.diningcode.com',
        'Referer': 'https://www.diningcode.com/',
        'User-Agent': 'Mozilla/5.0'
    }
    res = requests.post(url, headers=chrome_header, data=data)
    res_dict = json.loads(res.text)
    no_result_found = res_dict['result_data'].get('poi_section', 'NO_RESULT')
    if no_result_found == 'NO_RESULT':
        return
    total_cnt = res_dict['result_data']['poi_section']['total_cnt']
    for ptr in range(0, min(int(100/20), int(total_cnt/20))):
        print(city_name + ' ptr : ' + str(ptr))
        offset = ptr*20
        time.sleep(random())
        data = {'query': city_name, 'from': offset, 'size': offset+20}
        response = requests.post(url, headers=chrome_header, data=data)
        response_dict = json.loads(response.text)
        for restaurantSummary in response_dict['result_data']['poi_section']['list']:
            rid = restaurantSummary['v_rid']
            name = restaurantSummary['nm']
            img_src = restaurantSummary['image']
            score = restaurantSummary['score']
            latitude = restaurantSummary['lat']
            longitude = restaurantSummary['lng']
            category = restaurantSummary['category']
            phone = restaurantSummary['phone']
            address = restaurantSummary['addr']
            is_duplicated = restaurants.get(restaurantSummary['v_rid'], 'NO_KEY')
            if is_duplicated == 'NO_KEY':
                restaurants[rid] = {'rid': rid, 'name': name, 'imgSrc': img_src, 'score': score,
                                    'latitude': latitude, 'longitude': longitude, 'category': category,
                                    'phone': phone, 'address': address}
            else:
                duplicated_restaurants[rid] = {'rid': rid, 'name': name, 'address': address}
    return
