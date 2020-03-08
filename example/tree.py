#!/usr/bin/python
# coding:utf-8

"""
@author: houjinkai
@contact: xx@xx.com
@software: PyCharm
@file: tree.py
@time: 2020/3/8 9:34
"""
from turtle import *
#set color mode:RGB
colormode(255)
lt(90)

lv=14
l=120
s=45

width(lv)

#set init_color RGB
r=0
g=0
b=0
pencolor(r,g,b)

penup()
bk(l)
pendown()
fd(l)
def draw_tree(l,level):
    global r,g,b
    #save the current pen width
    w=width()
    #set color
    r=r+1
    g=g+2
    b=b+3
    pencolor(r%200,g%200,b%200)

    l=3.0/4.0*l
    lt(s)
    fd(l)
    if level <lv:
        draw_tree(1,level+1)
    bk(l)
    lt(l)
    #restore the previouspen width
    width(w)
speed('fastest')
draw_tree(l,4)
done()