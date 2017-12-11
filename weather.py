#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

def get_weather():

    baseurl = "http://www.accuweather.com/en/cn/shanghai/106577/daily-weather-forecast/106577?day=1"

    headers = {
        'Host':'www.accuweather.com',
    'Referer':'http: // www.accuweather.com',
    'User-Agent':'Mozilla / 5.0(Macintosh;IntelMacOSX10_12_0) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 58.0.3029.110Safari / 537.36'
    }

    high_ex = re.compile(r'<span class="large-temp">([0-9]+)&deg;')

    low_ex = re.compile(r'<span class="small-temp">/([0-9]+)&deg;')

    text_ex = re.compile(r'<span class="cond">(.{,40})</span>')

    result = requests.get(baseurl,headers = headers).text

    high = re.findall(high_ex,result)[4]
    low = re.findall(low_ex,result)[0]
    textw = re.findall(text_ex,result)[0]

    weather = '今日天气: %s\n'%textw+'气温: %s℃ / %s℃'%(high,low)

    return weather

if __name__ == "__main__":
    print(get_weather())
