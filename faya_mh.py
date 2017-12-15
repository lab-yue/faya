#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import db

def get_mh(order):

    mon_dict = db.name('mh').get()

    if order in mon_dict:
        return mon_dict[order]["info"]
    else:
        alter_dict = db.name('mon_alter').get()

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

        mon_dict = db.name('mh').get()

        if  ori not in mon_dict:
            return '大概mhxx没有？'
        else:
            alter = db.name('mon_alter')

            alter_dict = alter.get()
            alter_dict[new] = ori
            alter.set(alter_dict)

            return '存好新名字了'

if __name__ == "__main__":
    #print(mh_alter("alter 天慧龙:高达"))
    print(get_mh("イビルジョー"))
   # print(get_mh("高达"))