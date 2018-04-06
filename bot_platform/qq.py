#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import _thread
import time
from datetime import datetime

from qqbot import QQBotSched as qqbotsched, RunBot
from qqbot import QQBotSlot as qqbotslot

import main
import private
from core import db
from core.Fconf import config
from lib.more import bilibili, wyy
from lib.simple import aqi, weather


@qqbotslot
def onQQMessage(bot, contact, member, content):
    global master_qq_name, nict_dict, group_name, my_members_name

    # print(master_qq, contact.qq)

    if bot.isMe(contact, member):
        return

    nickname = '?'

    if member:
        # if int(member.qq) in my_members:
        #    nickname = my_members[int(member.qq)]
        # else:
        #    nickname = '?'
        for each in my_members_name:
            if each in member.nick:
                nickname = my_members_name[each]
                # else:
                #    nickname = '?'
    elif contact.mark == master_qq_name:
        # print('master~')
        nickname = 'master'
    else:
        nickname = '?'

    # print(nickname)

    '''
    if nickname in nick_dict:
        to_show_memo = check_memo(nickname)
        for each_p in to_show_memo:
            for each_memo in to_show_memo[each_p]:
                show_memo = '%s' % each_memo['memo']
                print(show_memo)
                bot.SendTo(contact, show_memo)
    '''

    faya_reply = main.scenario(nickname, content, contact)

    global last_post_time, last_reply

    if faya_reply:
        if last_reply == faya_reply:
            if time.time() - last_post_time > 20:
                bot.SendTo(contact, faya_reply)

                last_post_time = time.time()
                last_reply = faya_reply
        else:
            bot.SendTo(contact, faya_reply)

            last_post_time = time.time()
            last_reply = faya_reply

    if member and not faya_reply:
        with open('log.txt', 'a+') as log:
            log.write(content.replace('\n', '') + '\n')

    private.run(nickname, content, contact, bot)

    if content.find("http://music.163.com/") >= 0:
        bot.SendTo(contact, '尝试收藏')
        _thread.start_new_thread(wait_wyy, (bot, contact, content, nickname,))

    # wyylink = give_wyy()
    # return '尝试收藏' #save_wyy(content, nickname)+'\n\n'+wyylink

    if content.startswith('alarm'):
        al = content.split(' ')
        if len(al) >= 2:
            print(al)
            try:
                wait = float(al[1])
                if len(al) == 2:
                    _thread.start_new_thread(alarm, (bot, contact, nickname, wait,))
                else:
                    _thread.start_new_thread(alarm, (bot, contact, nickname, wait, al[2]))
            except TypeError:
                bot.SendTo(contact, '时间不对')


def wait_wyy(bot, contact, content, nickname):
    driver = wyy.save_wyy(content, nickname)
    bot.SendTo(contact, driver)
    return 0


def alarm(bot, contact, nick, minute, msg=''):
    bot.SendTo(contact, '好的')
    time.sleep(60 * minute)
    if msg:
        bot.SendTo(contact, nick + ' 提醒时间到了\n' + msg)
    else:
        bot.SendTo(contact, nick + ' 提醒时间到了')
    return 0


'''
@qqbotslot
def onStartupComplete(bot):
    with open('re.txt', 'w') as r:
        r.write(''+'\n')


@qqbotslot
def onExit(bot, code, reason, error):
    while 1:
        with open('re.txt', 'r') as r:
            if r.read() == 'ok':
                bot.Restart()                    
                break
            else:
                time.sleep(60)
'''


@qqbotsched(hour='0,1,6,8,11,20', minute='00')  # 18,20,22,23
def clock(bot):
    nowhour = datetime.now().hour
    global group_qq
    gl = bot.List('group', group_name)
    if gl is not None and (nowhour == 0 or nowhour >= 6):
        for group in gl:
            trd = '%s点了www' % nowhour
            kqzl = 0
            if nowhour == 6:
                trd += '\n 早呀。好困。'
                bot.SendTo(group, trd)

                tenki = weather.get()
                bot.SendTo(group, tenki)

                kqzl = aqi.get()
                bot.SendTo(group, kqzl)

            if nowhour == 11:
                trd += '\n中午了呢'

            if nowhour == 20:
                oral = db.name('oral')
                oral_db = oral.get()

                day_key = list(oral.get())[0]
                push = '今日口语: ' + day_key + '\n' + oral_db[day_key]
                oral_db.pop(day_key)
                oral.set(oral_db)

                bot.SendTo(group, push)

            if nowhour == 0:
                trd += '\n什么都不想说了。。'

            if not kqzl:
                bot.SendTo(group, trd)


ani_post = db.name('bili').get()

days, hours, minutes = [], [], []

if ani_post:
    for each in ani_post:
        if ani_post[each]['day'] not in days:
            days.append(ani_post[each]['day'])
        if ani_post[each]['hour'] not in hours:
            hours.append(ani_post[each]['hour'])
        if ani_post[each]['minute'] not in minutes:
            minutes.append(ani_post[each]['minute'])


    @qqbotsched(day_of_week=','.join(days), hour=','.join(hours), minute=','.join(minutes))
    def anime(bot):
        now = datetime.now()
        weekday = datetime.weekday(datetime.now())
        global group_qq
        gl = bot.List('group', group_name)
        if gl is not None:
            for group in gl:
                key = str(weekday) + str(now.hour) + str(now.minute)
                if key in ani_post:
                    info = ani_post[key]['title']
                    info = info + '\n' + bilibili.get_bilibili(ani_post[key]['av_id'])
                    bot.SendTo(group, info)

if __name__ == "__main__":

    try:
        # master_qq = fconf.master_qq
        nict_dict = config.nick_dict
        # group_qq = fconf.group_qq
        # my_members = fconf.my_members
        master_qq_name = config.master_qq_name
        my_members_name = config.my_members_nick
        group_name = config.group_name

        last_post_time = 0
        last_reply = ''

        RunBot()

    except KeyError:
        # raise
        print('配置文件有误')
