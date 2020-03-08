#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: udp_clicent.py
@time: 2020/3/8 10:45
"""
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Michael',b'Tracy',b'Sarah']:
    #send data
    s.sendto(data,('127.0.0.1',9999))
    #recieve data
    print(s.recv(1024).decode('utf-8'))
s.close()