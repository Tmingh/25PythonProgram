#!/usr/bin/env python
# coding=utf-8
from PIL import Image, ImageDraw, ImageFont
import sys

def add_num(imageName):
    im = Image.open(imageName)
    draw = ImageDraw.Draw(im)
    w, h = im.size
    font = ImageFont.truetype('Kim\'s GirlType.ttf',int(w/8))
    draw.text((int(w*5/6), 10), '99', font=font, fill=(255, 0, 0))
    outName = 'output_%s'%imageName
    im.save(outName, 'jpeg')

for name in sys.argv[1:]:
    add_num(name)

