# -*- coding: utf-8 -*-

import requests
import re


def get(word):
    sta_reg = re.compile(r'<div id="resultCount">[\s\S]+?</p>')
    word_reg = re.compile(r'<dl id="wordBody" class="text-l">[\s\S]+?</div>')

    headers = {
        'Host': 'www.sanseido.biz',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Referer': 'https://www.sanseido.biz/',
        'Connection':'close'
    }

    s = requests.session()
    s.keep_alive = False

    url = f'https://www.sanseido.biz/User/Dic/Index.aspx?TWords={word}&st=0&DORDER=&DailyJJ=checkbox&DailyEJ=checkbox&DailyJE=checkbox'

    t = s.get(url, headers=headers).text

    st = re.findall(sta_reg, t)[0]

    no_result = '一致する情報は見つかりませんでした'
    if no_result in st:
        return no_result
    else:
        raw = re.findall(word_reg, t)[0]

        html_reg = re.compile('<.+?>')
        b_reg = re.compile('\s')

        raw = html_reg.subn('', raw)[0]
        raw2 = b_reg.subn(' ', raw)[0]

        newline = [
            '（１）',
            '（２）',
            '（３）',
            '（４）',
            '（５）',
            '（６）',
            '▼',
            '・～'
        ]

        for each in newline:
            if each in raw2:
                raw2 = raw2.replace(each, '\n' + each)

        raw2 = raw2.replace('  ', '')

        return '検索結果:\n' + raw2

if __name__ == '__main__':
    try:
        print(get('ムニエル'))
    except :
        print('出了点问题')



#print(get_jp('恋'))

