#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


# import re


def get_aqi(city='sh'):
    city_dict = {
        'sh': '1437',
        'lz': '1405',
        'nj': '1485',
        'gz': '1449'
    }

    h = {'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
         'Upgrade-Insecure-Requests': '1',
         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
         'Cache-Control': 'max-age=0', 'Connection': 'keep-alive'}

    if city in city_dict:
        cityidx = city_dict[city]
    else:
        # city = city
        return '尚不支持此keyword'
    '''
    now = requests.get(f'http://www.86pm25.com/city/{city}.html').text  # headers = headers
    aqi_re = re.compile('var idx = "([0-9]+?)"')
    aqi = re.findall(aqi_re,now)
    '''
    now = requests.get(f'https://api.waqi.info/api/feed/@{cityidx}/now.json', headers=h).json()
    print(now)
    rxs = now.get('rxs', '')
    aqi = 0
    if rxs:
        obs = rxs.get('obs', '')
        if obs:
            aqi = obs[0]['msg']['aqi']
            update = obs[0]['msg']['time']['s']
            try:
                city_name = obs[0]['city']['name']
            except KeyError:
                city_name = obs[0]['msg']['city']['name']
            finally:
                pass

    if aqi == '-':
        return '无数据..'
    else:
        if aqi < 50:
            level = 'Good'
        elif aqi < 100:
            level = 'Moderate'
        elif aqi < 150:
            level = 'Relaitvely Unhealthy'
        elif aqi < 200:
            level = 'Unhealthy'
        elif aqi < 300:
            level = 'Very Unhealthy'
        else:
            level = 'Hazardous'

        msg = f'''现在{city_name}空气质量:\naqi: {aqi}\n评价: {level}\n更新于 {update}'''

        return msg

        # try:
        # aqi = int(aqi[0])

        # return 'oops 好像数据有问题'


if __name__ == "__main__":
    print(get_aqi('sh'))
