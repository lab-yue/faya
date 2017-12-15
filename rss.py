#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import feedparser
import db

def check():
    msg = ''
    feed = db.name('feed')
    sites = feed.get()
    for site in sites:
        d = feedparser.parse(sites[site]['url'])
        content = sites[site]['content']
        for each in d.entries[:3]:
            if each.title not in content:
                content[each.title] = each.link
                msg += f'{each.title} {each.link}\n'
                print(msg)

    if msg:
        feed.set(sites)
        return msg
    else:
        return '全部已读(~￣△￣)~'

if __name__ == '__main__':
    print(check())