#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core import db, sock


def send_wx(to_buddy_abb, msg):

    wx = db.name('wx').search('short', to_buddy_abb)

    if wx:
        #print(wx['wx'])
        sock.send(wx['wx'] + '@@@' + msg, 'wx')
    else:
        return '联系人错误orz'


    return '发送成功'

if __name__ == "__main__":
    print(send_wx('ma', 'try'))
