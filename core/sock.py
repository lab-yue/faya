#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time

def send(msg, app):
    ports= {'line':9998,'wx': 9999}
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', ports[app]))
    print(s.recv(1024).decode('utf-8'))
    data = bytes(msg, encoding="utf8")
    s.send(data)
    print('data ok')
    s.send(b'exit')
    s.close()

def sock_receive(sock, addr):
    sock.send(b'simple~!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        info = data.decode('utf-8')
        if 'exit' not in info:
            return info
        else:
            return info.replace('exit', '')
    sock.close()
    print('Connection closed.')
