#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import yaml
import re
from Fconf import Conf

def get_ydword(word):

    #conf =  str(Conf.yd)
    with open('faya.yml','r') as yml:
        conf = yaml.load(yml)['yd']

    url = f'http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=json&version=1.1&q='%(conf['keyfrom'],conf['key']) + word
    r = requests.get(url).json()
    if 'basic' in r:
        outcome = '查询结果为：\n'
        for each in r['basic']['explains']:
            outcome += each + '\n'
        return outcome.strip()

    elif 'web'in r:
        outcome = '查询web结果为：\n'

        for webex in r['web']:
            outcome += webex['value'][0] + '\n'
        return outcome.strip()
    else:
        return '并没有查到(｡ ́︿ ̀｡)'

def get_phon(pharse, nation):

    en_reg = re.compile('[a-zA-Z]+')

    words = re.findall(en_reg, pharse)

    out = ''

    for each in words:
        now = each.lower()
        out =out + get_word(now, nation) + ' '

    return out


def get_word(word, nation):

    with open('faya.yml','r') as yml:
        conf = yaml.load(yml)['yd']

    url = f'http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=json&version=1.1&q='%(conf['keyfrom'],conf['key']) + word
    r = requests.get(url).json()
    if 'basic' in r:
        base = r['basic']

        if 'us-phonetic' in base and nation == 'us':
            us = base['us-phonetic']
            return f'/{us}/'

        elif 'uk-phonetic' in base and nation == 'uk':
            uk = base['uk-phonetic']
            return f'/{uk}/'
        else:
            return '**'
    else:
        return '**'

if __name__=="__main__":
    print(get_ydword('hangar'))
    #print(get_phon('but one man loved the sorrows of your changing face', 'us'))