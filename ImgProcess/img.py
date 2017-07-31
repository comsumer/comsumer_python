from PIL import Image, ImageDraw, ImageFont

import sys, os

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
print cur_file_dir()


def add_num(filePath, num=1):
    img = Image.open(filePath)
    size = img.size
    fontsize = size[1]/4
    print fontsize
    myfont = ImageFont.truetype('calibri.ttf', fontsize)
    ImageDraw.Draw(img).text((2 * fontsize, 0), str(num), font = myfont, fill = 'red')
    img.save('D:\\work\\MYPYProject\\ImgProcess\\desert_added.jpg')
    img.show()

add_num('D:\\work\\MYPYProject\\ImgProcess\Desert.jpg',num=1)
