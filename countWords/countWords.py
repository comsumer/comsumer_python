#!/usr/local/bin/python
#coding=utf-8

#正则表达式统计单词个数
import re

def count_words(filepath):
    assert isinstance(filepath, object)
    f = open(filepath)
    text = f.read()
    #r表示不进行任何转义,[xxx]+表示满足框内条件的尽可能长的串,可以考虑下findall的算法
    wordlist = re.findall(r'[a-zA-Z]+',text)
    count = len(wordlist)
    return count

#执行语句
nums = count_words('D:\\work\\MyPYProject\\countWords\\file.txt')
print nums
