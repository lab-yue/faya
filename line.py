# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from Faya_fun import scenario
import _thread
from sock import *
import yaml

app = Flask(__name__)

with open('faya.yml','r') as yml:
    conf = yaml.load(yml)
line_conf = conf['line']
channel_secret = line_conf['channel_secret']
channel_access_token = line_conf['channel_access_token']
master = line_conf['master']
push_key = line_conf['push']

line_bot_api = LineBotApi(channel_access_token, timeout=10)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    events = ''

    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        if event.source.sender_id == master:
            nickname = 'master'
        else:
            nickname = '?'

        #try:
        txt = scenario(nickname, event.message.text, '')
        #except:
        #    txt = '在line中的faya暂时不支持此命令'

        if txt:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=txt))

    return 'OK'

def line_push(msg):
    line_bot_api.push_message(push_key, TextSendMessage(text=msg))

def push():
    while True:
        sock, addr = s.accept()
        info = sock_receive(sock, addr)
        line_push(info)

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9998))
    s.listen(5)
    print('已在9998开启端口')

    _thread.start_new_thread(push, ())

    app.run(debug=options.debug, port=options.port)
