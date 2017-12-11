#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import time
from datetime import datetime

class timer(object):

    def __init__(self):
        self.apple = 'A apple'

    def start(self,joke):

        event = joke[0]
        nickname = joke[1]

        start_time = time.time()
        now = datetime.fromtimestamp(start_time)

        timer_key = nickname + event + '_timer'

        mark_key = event + '_timer'

        with open(nickname + '.json', 'r') as marked:
            marked_dict = json.loads(marked.read())

        marked_dict[mark_key] = start_time

        with open('data/' + nickname + '.json', 'w') as outfile:
            json.dump(marked_dict, outfile, ensure_ascii=False)
            outfile.write('\n')

        with open('data/timer.json', 'r') as time_dict:
            time_dict = json.loads(time_dict.read())

        if timer_key not in time_dict:
            time_dict[timer_key] = {}

        with open('timer.json', 'w') as outfile:
            json.dump(time_dict, outfile, ensure_ascii=False)
            outfile.write('\n')

        return event + ' 计时开始于 ' + str(now).split('.')[0]

    def pause(self, joke):

        event = joke[0]
        nickname = joke[1]

        timer_key = nickname + event + '_timer'
        mark_key = event + '_timer'

        with open('data/'+nickname + '.json', 'r') as marked:
            marked_dict = json.loads(marked.read())

        with open('data/timer.json', 'r') as time_dict:
            time_dict = json.loads(time_dict.read())

        if mark_key in marked_dict :

            start = marked_dict[mark_key]

            new_time_list = timer.duration(self,mark_key, marked_dict)

            if 'alltime' in time_dict[timer_key]:
                time_dict[timer_key]['alltime'] = timer.time_adder(self,time_dict[timer_key]['alltime'],new_time_list)

            else:time_dict[timer_key]['alltime'] = new_time_list

            if 'today' in time_dict[timer_key]:
                time_dict[timer_key]['today'] = timer.time_adder(self,time_dict[timer_key]['today'],new_time_list)

            else:time_dict[timer_key]['today'] = new_time_list

            reply = timer.time_cn(self,time_dict[timer_key]['alltime'])
            result = event + ' 计时暂停，共 ' + reply

            with open('data/'+nickname + '.json', 'w') as outfile:
                json.dump(marked_dict, outfile, ensure_ascii=False)
                outfile.write('\n')

            with open('data/'+'timer.json', 'w') as outfile:
                json.dump(time_dict, outfile, ensure_ascii=False)
                outfile.write('\n')

        else :
            result = event + '未开始'

        return result

    def stop(self, joke):

        event = joke[0]
        nickname = joke[1]

        mark_key = event + '_timer'

        timer_key = nickname + event + '_timer'
        reply =  timer.pause(self,joke).replace('暂停','停止')

        with open('data/'+'timer.json', 'r') as time_dict:
            time_dict = json.loads(time_dict.read())

        with open('data/'+nickname + '.json', 'r') as marked:
            marked_dict = json.loads(marked.read())

        marked_dict.pop(mark_key)

        with open('data/'+nickname + '.json', 'w') as outfile:
            json.dump(marked_dict, outfile, ensure_ascii=False)
            outfile.write('\n')

            if 'alltime' in time_dict[timer_key]:
                time_dict[timer_key]['alltime'] = [0, 0, 0, 0]

        with open('data/timer.json', 'w') as outfile:
            json.dump(time_dict, outfile, ensure_ascii=False)
            outfile.write('\n')

        return reply

    def clean(self):

        with open('data/timer.json', 'r') as time_dict:
            time_dict = json.loads(time_dict.read())

        with open('data/timer_history.json', 'r') as timer_history:
            history_dict = json.loads(timer_history.read())

        history = {}

        date = datetime.fromtimestamp(time.time())

        for each in time_dict:

            if time_dict[each]['today'][2] > 0 and time_dict[each]['today'][0] < 1:
                history[each] = time_dict[each]['today']

        history_dict[str(date.month) + '.' + str(date.day)] = history


        for each in time_dict:
            time_dict[each]['today'] = [0, 0, 0, 0]

        with open('data/timer_history.json', 'w') as outfile:
            json.dump(history_dict, outfile, ensure_ascii=False)
            outfile.write('\n')

        with open('data/timer.json', 'w') as outfile:
            json.dump(time_dict, outfile, ensure_ascii=False)
            outfile.write('\n')


        return '已重置today'

    def cn_reply(self,timer_key,marked_dict):

        timed = timer.duration(self,timer_key, marked_dict)
        return timer.time_cn(self,timed)

    def now(self, joke):

        event = joke[0]
        nickname = joke[1]

        timer_key = nickname + event + '_timer'

        mark_key = event + '_timer'

        with open('data/'+nickname + '.json', 'r') as marked:
            marked_dict = json.loads(marked.read())

        with open('data/timer.json', 'r') as time_dict:
            time_dict = json.loads(time_dict.read())

        if mark_key in marked_dict:


            if timer_key in time_dict and 'alltime' in time_dict[timer_key]:

                reply = timer.time_cn(self, time_dict[timer_key]['alltime'])

                return event + ' 暂停中，目前 ' + reply

            else:
                reply = timer.cn_reply(self,mark_key, marked_dict)

                return event + ' 目前计时，本次共 ' + reply

        else:
            return event +' 未开始'

    def today(self,nickname):

        with open('data/timer.json', 'r') as time_dict:
            time_dict = json.loads(time_dict.read())

        today_list = []

        message = nickname + '今天一共'

        for each in time_dict:

            reckon = each.replace('_timer', '_r')

            if (nickname in each) and ('today' in time_dict[each]):



                if time_dict[each]['today'][2] > 0 and time_dict[each]['today'][0] < 1:
                    item = timer.time_cn(self,time_dict[each]['today'])

                    each_r = each.replace(nickname,'')
                    each_r = each_r.replace('_timer','')

                    today_list.append('\n' + each_r + ' ' + item)

            if '_r' in each:

                reckoned = timer.time_cn(self, time_dict[each])
                reckon_k = reckon.replace(nickname, '')
                reckon_k = reckon_k.replace('_r', '')
                today_list.append('\n原预计 ' + reckon_k + ' ' + reckoned)

        for each in today_list:
            message  += each

        if today_list == []:
            message = nickname + '今天什么都还没记录呢'

        return message

    def reckon(self,joke,time):

        event = joke[0]
        nickname = joke[1]

        with open('data/timer.json', 'r') as time_dict:
            time_dict = json.loads(time_dict.read())

        if time[1] < 24 :
            time_dict[nickname+event+'_r'] = time
        else: return '预计应小于24小时哦'

        with open('data/timer.json', 'w') as outfile:
            json.dump(time_dict, outfile, ensure_ascii=False)
            outfile.write('\n')

        return '预计 '+event+' 使用 '+ timer.time_cn(self,time)

    def cancel(self, joke):

        event = joke[0]
        nickname = joke[1]

        r_key = nickname + event + '_r'

        with open('data/timer.json', 'r') as time_dict:
            time_dict = json.loads(time_dict.read())

        if r_key in  time_dict:
            time_dict.pop(r_key)

            with open('data/timer.json', 'w') as outfile:
                json.dump(time_dict, outfile, ensure_ascii=False)
                outfile.write('\n')

            return '已取消 '+event+' 的预计'
        else:
            return  '还没有预计' +  event



    def duration(self,timer_key,marked_dict):

        start = marked_dict[timer_key]

        finish = time.time()
        dur = (datetime.fromtimestamp(finish) - datetime.fromtimestamp(start))

        day = dur.days
        hour = dur.seconds // 3600
        minute = (dur.seconds - 3600 * hour) // 60
        second = dur.seconds % 60

        return [day,hour,minute,second]

    def time_cn(self,time):

        (day,hour,minute,second) = time

        message =''

        if day > 0:
            message += str(day) + ' 天 '
        if hour > 0:
            message += str(hour) + ' 小时 '
        if minute > 0:
            message += str(minute) + ' 分钟 '
        else:
            message += str(second) + ' 秒'

        return message

    def time_adder(self,list1,list2):

        new_list = []

        for x in range(0,4):
            new_list.append(list1[x]+list2[x])

        if new_list[3]>60:
            new_list[3] -= 60
            new_list[3] += 1
        if new_list[2]>60:
            new_list[2] -= 60
            new_list[1] += 1
        if new_list[1] > 24:
            new_list[1] -= 24
            new_list[0] += 1

        return new_list

if __name__=="__main__":
    #print(timer_hajime('test','主人'))
    #time.sleep(5)

    timer = timer()
    #print(timer.clean())

    print(timer.clean())
'''
    print(timer.start(['test', 'haru']))
    time.sleep(1)
    print(timer.now(['test', 'haru']))
    time.sleep(1)
    print(timer.pause(['test', 'haru']))
    print(timer.now(['test', 'haru']))
    print(timer.today('haru'))
    time.sleep(1)
    print(timer.stop(['test', 'haru']))
'''

