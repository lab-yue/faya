# import timerOOP

# timer = timerOOP.timer()


def a(content, nickname, timer):
    faya_reply = ''
    if content[-3:] == ".on":
        to_timer = content.replace('.on', '')
        faya_reply = timer.start([to_timer, nickname])

        if to_timer == 'sleep':
            faya_reply = '好好休息，' + nickname + '。 ' + faya_reply

    if content[-4:] == ".now":
        to_timer = content.replace('.now', '')
        faya_reply = timer.now([to_timer, nickname])

    if content[-5:] == ".stop":
        to_timer = content.replace('.stop', '')
        faya_reply = timer.stop([to_timer, nickname])
        if to_timer == 'sleep':
            faya_reply = '起来啦，' + nickname + '。' + faya_reply

    if content == "timer.today":
        faya_reply = timer.today(nickname)

    return faya_reply
