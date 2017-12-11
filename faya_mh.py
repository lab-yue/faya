#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def get_mh(order):

    with open('mh.json', 'r', encoding='utf-8') as mh:
        mon_dict = json.loads(mh.read())

    if order in mon_dict:
        return mon_dict[order]["info"]
    else:

        with open('mon_alter.json', 'r', encoding='utf-8') as mh:
            alter_dict = json.loads(mh.read())

            if order not in alter_dict:

                for each in mon_dict:
                    if order == mon_dict[each]["jp_name"]:
                        return mon_dict[each]["info"]

                return "大概没有？"

            else:
                return mon_dict[alter_dict[order]]["info"]


def mh_alter(order):
    if ':' not in order:
        return '……噫'
    else:
        tep = order.replace('alter ', '')
        ori,new = tep.split(':')

        print(ori,new)

        with open('mh.json', 'r', encoding='utf-8') as mh:
            mon_dict = json.loads(mh.read())

        if  ori not in mon_dict:
            return '大概mhxx没有？'
        else:
            with open('mon_alter.json', 'r', encoding='utf-8') as mh:
                alter_dict = json.loads(mh.read())

            alter_dict[new] = ori

            with open('mon_alter.json', 'w') as outfile:
               json.dump(alter_dict, outfile, ensure_ascii=False)
               outfile.write('\n')
            return '存好新名字了'

if __name__ == "__main__":
    #print(mh_alter("alter 天慧龙:高达"))
    print(get_mh("イビルジョー"))
   # print(get_mh("高达"))