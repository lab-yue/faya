#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def get(data):
    s = requests.session()
    s.keep_alive = False
    '''
    main_headers = {'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6,en;q=0.4',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Cache-Control': 'max-age=0'}
    html = s.get('https://ai.binwang.me/couplet/',headers=main_headers).text
    api_re = re.compile('get\("(http.+?chat/couplet/)" \+ self\.in_str')
    api = re.findall(api_re ,html)
    print(api)
    '''
    #if api:
    headers = {'Host': 'proxy.binwang.me:5001', 'Origin': 'http://ai.binwang.me',
                   'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6,en;q=0.4',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                   'Accept': '*/*', 'Referer': 'http://ai.binwang.me/couplet/', 'Connection': 'keep-alive'}

    try:
        xia = s.get(f'https://ai-backend.binwang.me/chat/couplet/{data}',headers=headers).json()
        if 'output' in xia:
            return '下联是 ' + xia['output']
        else:
            return '貌似没结果'
    except:
        return '貌似API变更了？'

if __name__ == '__main__':
    print(get('没睡好困'))

