import time
import urllib
import pandas as pd
import re
import csv
import requests

# url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
#
# params = {'query': "광주광역시 메가커피", 'page': 1}  # page 1번에서 "광주광역시 메가커피" 검색
# headers = {"Authorization": "KakaoAK e5f4009b56eefc9fc2a586afd528b354"}
# places = requests.get(url, params=params, headers=headers).json()['documents']
# total = requests.get(url, params=params, headers=headers).json()['meta']['total_count']
#
# for x in places:
#     print(x)
# print(total)
# print(len(places))

your_projectKey = 'co88tb8t9bebr_tp7b9et9t11p111_ct'
params = 'startDate=201609&endDate=201711'
url = f'https://open.jejudatahub.net/api/proxy/tDatbD61tD1tata3t3at3Dtt03D10D63/{your_projectKey}?{params}'
page_num = 1
cnt = 1

total = requests.get(url).json()['totCnt']
res_list = list()

while True:
    param_dict = {'number': page_num, 'limit': 100}

    response = requests.get(url, params=param_dict).json()['data']
    for i in response:
        print(cnt)
        print(i)
        cnt += 1
        res_list.append(i)
    if cnt >= total:
        break
    print("next")
    page_num += 1

for i in res_list:
    print(i)

df = pd.json_normalize(res_list)
df.to_csv("tourist_consumption.csv")

params = 'startDate=201609&endDate=201812'
url = f'https://open.jejudatahub.net/api/proxy/5D5a577taba7tbb71at1b1bt9tatata9/{your_projectKey}?{params}'
page_num = 1
cnt = 1

total = requests.get(url).json()['totCnt']
res_list = list()

while True:
    param_dict = {'number': page_num, 'limit': 100}

    response = requests.get(url, params=param_dict).json()['data']
    for i in response:
        print(cnt)
        print(i)
        cnt += 1
        res_list.append(i)
    if cnt >= total:
        break
    print("next")
    page_num += 1

for i in res_list:
    print(i)

df = pd.json_normalize(res_list)
df.to_csv("card_usage_korean.csv")
