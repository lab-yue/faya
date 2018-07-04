#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import html


def get(word):
    headers = {'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
              }

    page = requests.get(f'http://www.thesaurus.com/browse/{word}?s=t', headers=headers)
    tree = html.fromstring(page.text)
    part = tree.xpath('//*[@id="filters-0"]/div[3]/div/ul/li/a/span[1]')
    count = 0
    if not part:
        return '没找到的说'
    opt = '找到这些近义词:\n\n'
    for each in part:
        if count < 4:
            opt +=  '\t'+ each.text
            count += 1
        else:
            count = 0
            opt += '\n' + each.text

    return opt.replace('\t', '', 1)

if __name__ == '__main__':
    #print(find('wish').replace('\n','###').replace('\t','@@@'))
    print(get('wish'))

