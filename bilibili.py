#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import requests
import re
import json
import db

def add_bilibili(url):
    if 'anime/' in url:
        try:
            index = int(url.split('/')[-1])

            jsonp =  get_bilibili_api(index)['result']

            title = jsonp['bangumi_title']

            update_time = jsonp['media']['episode_index']['index_show']
            time_reg = re.compile('每周(.)(\d+?):(\d+)')
            info = re.findall(time_reg,update_time)[0]

            trans = {'一': '0',
                     '二': '1',
                     '三': '2',
                     '四': '3',
                     '五': '4',
                     '六': '5',
                     '日': '6',
             }
            this_ani = {
                'title':title,
                'av_id':index,
                'day':trans[info[0]],
                'hour':info[1],
                'minute':str(int(info[2]) + 5)
            }
            print(this_ani)

            data = db.name('bili')

            a = data.get()
            a[this_ani['day']+this_ani['hour']+this_ani['minute']] = this_ani
            data.set(a)

            return f'已获取{title}信息、{update_time}'
        except TypeError:
            return '貌似url不合法，最后是数字么？或者遇到了蜜汁bug……'

def get_bilibili_api(av_id):


    parturl = 'http://bangumi.bilibili.com/jsonp/seasoninfo/%s.ver?callback=seasonListCallback&jsonp=jsonp&_='%av_id + str(time.time()*10000)
    headers = {

        'Referer': 'http://bangumi.bilibili.com/anime/%s/'%av_id,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'X - Requested - With': 'XMLHttpRequest'
    }
    return json.loads(requests.get(parturl,headers = headers).text[19:-2])

def get_pagelist(av_id=16983061):
    headers = {'Origin': 'https://www.bilibili.com', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6,en;q=0.4', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Referer': f'https://www.bilibili.com/video/av{av_id}/'}
    now = requests.get(f'https://api.bilibili.com/x/player/pagelist?aid={av_id}&jsonp=jsonp',headers=headers).json()
    return '现在更新到：' + now['data'][-1]['part']

def get_bilibili(av_id):
    jsonp = get_bilibili_api(av_id)
    le = jsonp['result']['episodes'][0]
    realurl = 'http://www.bilibili.com/video/av'
    if le:
        msgbk = '第%s集: '%le['index']+le['index_title']+'\n'+realurl+le['av_id']+'\n'
        msgbk = msgbk.strip()

        return msgbk

if __name__=="__main__":
    print(get_bilibili_api('https://bangumi.bilibili.com/anime/22504'))
