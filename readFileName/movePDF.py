#!/usr/local/bin/python
#coding=utf-8

import os

path ='D:\\pdfTransfer\\ImgUp\\'
newPath='D:\\pdfTransfer\\ImgGet\\'

for (path, dirs, files) in os.walk(path):
    for filename in files:
        #print filename

        #组建新的文件名
        newname1= filename[19:37] +'000.pdf'
        newname2 =filename[19:36]+'1.pdf'

        #组建带路径的文件名
        oldfile = path + '\\' +filename

        relaDir =path[-8:-1] +path[-1]
        newdir = newPath+relaDir

        newfile1 = newdir +'\\' + newname1
        newfile2 = newdir + '\\' + newname2

        if not os.path.exists(newdir):
            os.mkdir(newdir)

        ret=os.system("copy %s %s" % (oldfile, newfile1))
        os.system("copy %s %s" % (oldfile, newfile2))



