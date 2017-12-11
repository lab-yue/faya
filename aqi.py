#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

def get_aqi(city='sh'):
    cityname = city

    city_dict = {
        'sh': 'shanghai',
        'lz': 'lanzhou',
        'nj': 'nanjing',
    }

    if cityname in city_dict:
        city = city_dict[cityname]
    else:
        return '尚不支持此keyword'
    now = requests.get(f'http://www.86pm25.com/city/{city}.html').text  # headers = headers
    aqi_re = re.compile('var idx = "([0-9]+?)"')
    aqi = re.findall(aqi_re,now)
    try:
        aqi = int(aqi[0])

        if aqi < 50:
            Level = 'Good'
        elif aqi < 100:
            Level = 'Moderate'
        elif aqi < 150:
            Level = 'Relaitvely Unhealthy'
        elif aqi < 200:
            Level = 'Unhealthy'
        elif aqi < 300:
            Level = 'Very Unhealthy'
        else:
            Level = 'Hazardous'

        msg = f'现在{city}空气质量:\naqi: %s' % aqi  + '\n' + '评价: %s' % Level

        return msg
    except:
        return 'oops 好像数据有问题'

if __name__=="__main__":
    print(get_aqi('lz'))
