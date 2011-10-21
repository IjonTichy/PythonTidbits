#!/usr/bin/python3

import shutil, os

oldStart = 'HNT'
newStart = 'UBF'


ls = os.listdir('.')
playersprites = []

for image in ls:
    if image.startswith(oldStart):
        newname = newStart + image[len(oldStart):]

        playersprites.append((image, newname))
        print newname

for (oldname, newname) in playersprites:
    shutil.move(oldname, newname)
