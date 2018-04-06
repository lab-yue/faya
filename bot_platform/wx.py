#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import _thread
import os

import itchat
from core.Fconf import config
from core import db
from core.sock import socket, sock_receive
from main import scenario

with open('faya.yml', 'r') as yml:
    conf = config.wx

self = conf['self']

data = db.name('wx').get()


@itchat.msg_register('Text')
def text_reply(msg):
    from_who = msg['FromUserName']

    from_buddy = itchat.search_friends(userName=from_who)['NickName']

    print(from_buddy)

    content = msg['Text']
    '''
    if from_buddy == self and content == 'reqq':
        with open('re.txt', 'w') as re:
            re.write('ok')
        msg.user.send('尝试重启')
    '''

    if from_buddy in data:

        nick = data[from_buddy]['display']

        save = data[from_buddy]['short']

        with open('wx.txt', 'w') as last:
            last.write(save)

        if nick == 'dalao':

            try:
                txt = scenario('tf', content, '')
            except:
                txt = '暂时不支持此命令'

            if txt:
                msg.user.send(txt)

            wx_msg = f'有来自 {nick} 微信消息：{content}'

            os.system(f"qq send buddy master {wx_msg}")
        else:
            wx_msg = f'有来自 {nick} 微信消息：{content}'
            os.system(f"qq send buddy master {wx_msg}")


@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video', 'Map', 'Card', 'Note', 'Sharing'])
def atta_reply(msg):
    from_who = msg['FromUserName']

    from_buddy = itchat.search_friends(userName=from_who)['NickName']

    wx_type = msg['Type']

    if from_buddy in data:
        nick = data[from_buddy]['display']

        wx_msg = f'有来自 {nick} 微信的{wx_type}消息'

        os.system(f"qq send buddy master {wx_msg}")


itchat.auto_login()

_thread.start_new_thread(itchat.run, ())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('已在9999开启端口')

while True:
    sock, addr = s.accept()
    info = sock_receive(sock, addr).split('@@@')
    to_buddy = itchat.search_friends(nickName=info[0])[0]
    to_buddy.send(info[1])
