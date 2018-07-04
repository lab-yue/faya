# -*- coding: UTF-8 -*-

import requests
from datetime import datetime


def get():
    msg = ''
    today = str(datetime.now()).split(" ")[0]
    base = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id='
    headers = {'Pragma': 'no-cache',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
               'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Referer': 'https://www.pixiv.net/idea/',
               'X-Requested-With': 'XMLHttpRequest',
               'Connection': 'keep-alive',
               'Cache-Control': 'no-cache'
               }
    response = requests.get(
        f'https://www.pixiv.net/ajax/idea/anniversary/{today}', headers=headers
    )
    data = response.json()
    if not data.get('error', True):
        body = data.get('body')
        tag = body['idea_anniversary_tag']
        description = body['idea_anniversary_description']
        example = base + body['popular_illust']['illust_id']  # ['url']['600x1200']

        msg = f'今日题目是 {tag}\n\n{description}\n{example}'

    return msg


if __name__ == '__main__':
    print(get())
