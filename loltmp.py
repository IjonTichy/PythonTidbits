#!/usr/bin/env python3

from random import randrange

choicesLeft   = 10
choices       = choicesLeft
chosenAlready = [False]*choicesLeft

while True:

    choice = randrange(1, choices+1)

    if not chosenAlready[choice-1]:

        print("Choice {0} reached".format(choice))
        choicesLeft -= 1
        chosenAlready[choice-1] = True

    if choicesLeft == 0:
        break
