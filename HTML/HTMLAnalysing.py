#!/usr/bin/python
#coding=utf-8

"""
第 0008 题：一个HTML文件，找出里面的正文。

"""

from bs4 import BeautifulSoup
import urllib2

def find_the_content(path):
    with open(path) as f:
        text = BeautifulSoup(f, 'lxml')
        content = text.get_text().strip('\n')
        print content
        return content.encode('gbk','ignore')

def find_the_links(path):
    with open(path) as f:
        soup = BeautifulSoup(f,'lxml')
        for link in soup.find_all('a'):
            print(link.get('href'))

def baidu_content():
    url = "https://www.baidu.com"
    page = urllib2.urlopen(url,'lxml')
    soup = BeautifulSoup(page,'lxml')
    print soup.body.text

def baidu_link():
    url = "https://www.baidu.com"
    page = urllib2.urlopen(url, 'lxml')
    soup = BeautifulSoup(page,'lxml')
    #格式化打印
    print soup.prettify()
    links = soup.findAll('a')
    for link in links:
        print(link['href'])

def test_soup():
    with open('D:\\work\\MyPYProject\\HTML\\1.html') as f:
        soup = BeautifulSoup(f, 'lxml')
        print soup.prettify()

if __name__ == '__main__':
    #find_the_content('D:\\work\\MyPYProject\\HTML\\1.html')
    #find_the_links('https://www.google.com')
    #baidu_content()
    #baidu_link()
    test_soup()