#!/usr/bin/python3
# -*- coding: utf-8 -*-

import string
import textwrap
import codecs

import random

class NotASCII(Exception): pass

WORDCOUNT = 5000

dictFile  = codecs.open("/usr/share/dict/en_US.dic", "r", encoding="utf-8")
dictWords = []


for i in dictFile:

    i = i.strip()

    try:
        for j in i:
            if j not in string.ascii_lowercase:
                raise NotASCII

    except NotASCII:
        continue

    if len(i) > 10 or len(i) < 3:
        continue

    dictWords.append(i)


chosenWords = []
wordcount   = 0

while wordcount != WORDCOUNT:   # hurr same name
    nextWord = random.randrange(0, len(dictWords) )
    newWord = dictWords.pop(nextWord)

    chosenWords.append(newWord)
    wordcount += 1

    if len(dictWords) == 0:
        break



wrapper = textwrap.TextWrapper()
wrapper.width = 80

wrappedText = wrapper.wrap("""{{"{0}"}}""".format("\", \"".join(chosenWords) ) );


for line in wrappedText:
    print(line)
