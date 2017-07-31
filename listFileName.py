#!/usr/local/bin/python
#coding=utf-8
import os


fileName = os. listdir('D:\\work\\lbm')

#注意open的参数是文件名不是文件路径
f = open('lbm.txt', 'wb')

i = len(fileName)
while i>1:
    s=fileName.pop(i-1)
    s = s[:-4]
    i=i-1
    f.write(s +'\n')
f.close()





