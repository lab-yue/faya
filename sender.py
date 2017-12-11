#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sock import *

def send_wx(to_buddy_abb, msg):

    nickdict = ''

    if to_buddy_abb in nickdict:
        to_buddy = nickdict[to_buddy_abb]
    else:
        return '联系人错误orz'

    soc(to_buddy + '@@@' + msg, 'wx')

    return '发送成功'

if __name__ == "__main__":
    print(send_wx('ma', 'try'))
