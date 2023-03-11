import requests
import base64
import json
from bs4 import BeautifulSoup

if __name__ == '__main__':
    print("hello world!")
    data = {'query': '선릉역', 'page': 0, 'size': 20}
    URL = 'https://im.diningcode.com/API/isearch/'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '39',
        'Content-Type': 'gzip, deflate, br',
        'Host': 'im.diningcode.com',
        'Origin': 'https://www.diningcode.com',
        'Referer': 'https://www.diningcode.com/',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'macOS',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    inhyeok_header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'PostmanRuntime / 7.31.1',
    }
    headersInPostman ={
        'User-Agent': 'PostmanRuntime / 7.31.1',
        'Accept': '* / *',
        'Host': 'im.diningcode.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '39'
    }
    res = requests.post(URL, headers=headersInPostman, data=data)
    print(res.text)
    print(res)
    #print(webpage)
