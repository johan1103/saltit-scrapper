import time

import requests
import base64
import json
from bs4 import BeautifulSoup

if __name__ == '__main__':
    data = {'query': '선릉', 'from': 0, 'size': 20}
    URL = 'https://im.diningcode.com/API/isearch/'
    chrome_header = {
        'Accept': 'application/json, text/plain, */*',
        'Host': 'im.diningcode.com',
        'Origin': 'https://www.diningcode.com',
        'Referer': 'https://www.diningcode.com/',
        'User-Agent': 'Mozilla/5.0'
    }
    headersInPostman ={
        'User-Agent': 'PostmanRuntime / 7.31.1',
        'Accept': '* / *',
        'Host': 'im.diningcode.com',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    res = requests.post(URL, headers=headersInPostman, data=data)
    resDict = json.loads(res.text)
    totalCnt = resDict['result_data']['poi_section']['total_cnt']
    restaurants = {}
    duplicatedRestaurants = {}
    for ptr in range(0, int(totalCnt/20)):
        print(ptr)
        offset = ptr*20
        time.sleep(0.5)
        data = {'query': '선릉', 'from': offset, 'size': offset+20}
        response = requests.post(URL, headers=chrome_header, data=data)
        responseDict = json.loads(response.text)
        for restaurantSummary in responseDict['result_data']['poi_section']['list']:
            rid = restaurantSummary['v_rid']
            name = restaurantSummary['nm']
            imgSrc = restaurantSummary['image']
            score = restaurantSummary['score']
            latitude = restaurantSummary['lat']
            longitude = restaurantSummary['lng']
            category = restaurantSummary['category']
            phone = restaurantSummary['phone']
            address = restaurantSummary['addr']
            isDuplicated = restaurants.get(restaurantSummary['v_rid'], 'NO_KEY')
            if isDuplicated == 'NO_KEY':
                restaurants[rid] = {'rid': rid, 'name': name, 'imgSrc': imgSrc, 'score': score,
                                    'latitude': latitude, 'longitude': longitude, 'category': category,
                                    'phone': phone, 'address': address}
            else:
                duplicatedRestaurants[rid] = {'rid': rid, 'name': name, 'address': address,
                                              'duplicatedCnt': 0}

    f = open("static/scrap.txt", 'w')
    for rid in restaurants:
        print(rid)
        f.write('id : ')
        f.write(restaurants[rid]['rid'])
        f.write(', name : ')
        f.write(restaurants[rid]['name'])
        f.write(', location : {')
        f.write(str(restaurants[rid]['latitude']))
        f.write(', ')
        f.write(str(restaurants[rid]['longitude']))
        f.write('}')
        f.write('\n')
    f.close()
    print('-----------duplicated----------')
    f = open("static/duplicated.txt", 'w')
    for rid in duplicatedRestaurants:
        print(rid)
        f.write('id ')
        f.write(duplicatedRestaurants[rid]['rid'])
        f.write(' name ')
        f.write(duplicatedRestaurants[rid]['name'])
        f.write('\n')
    f.close()