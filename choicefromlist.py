#!/usr/bin/env python

from types import FunctionType, BuiltinFunctionType, ModuleType
from inspect import isclass
from math import log

__all__ = ["funcdir", "choiceFromList"]

def funcdir(module):
    for desc in dir(module):
        desc2 = getattr(module, desc, None)

        if isinstance(desc2, (FunctionType, BuiltinFunctionType)) or isclass(desc2):
            yield desc2


def choiceFromList(choices, *args, prompt="choice:", unpackArgs=False):

    if isinstance(choices, ModuleType):
        choices = list(funcdir(choices))

    choice      = -1
    choiceCount = len(choices)
    spaceCount  = int(log(choiceCount, 10))

    for l, i in enumerate(choices):
        spaceCount2 = int( log(max(1, l+1), 10) )-1

        # print(spaceCount, spaceCount2)
        print("({0}){1:>{2}}{3}".format(l+1, " ", spaceCount-spaceCount2,
                                         i.__name__) )

    while choice == -1:

        try:
            choice = int(input(prompt+" "))

        except (TypeError, ValueError):
            choice = -1

        if (choice < 1) or (choice > choiceCount):
            choice = -1

    choice -= 1

    if unpackArgs:
        result = choices[choice](*args)
    else:
        result = choices[choice](args)

    print(result)


if __name__ == "__main__":
    choiceFromList([bin, oct, int, hex, bytes, str, tuple, bytearray, list,
                    set, sum, all, any, ],
                   "943", unpackArgs=1)

    input("\n\n<enter>")
