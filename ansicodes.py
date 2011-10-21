#!/usr/bin/env python3

RESET               = "\033[0m"

BOLDON              = "\033[1m"
BOLDOFF             = "\033[22m"

DIMON               = "\033[2m"
DIMOFF              = "\033[21m"

ITALICSON           = "\033[3m"
ITALICSOFF          = "\033[23m"

UNDERLINEON         = "\033[4m"
UNDERLINEOFF        = "\033[24m"

INVERSEON           = "\033[7m"
INVERSEOFF          = "\033[27m"

STRIKETHROUGHON     = "\033[7m"
STRIKETHROUGHOFF    = "\033[27m"

BLACKF              = "\033[30m"
REDF                = "\033[31m"
GREENF              = "\033[32m"
YELLOWF             = "\033[33m"
BLUEF               = "\033[34m"
MAGENTAF            = "\033[35m"
CYANF               = "\033[36m"
WHITEF              = "\033[37m"
DEFAULTF            = "\033[39m"

BLACKB              = "\033[40m"
REDB                = "\033[41m"
GREENB              = "\033[42m"
YELLOWB             = "\033[43m"
BLUEB               = "\033[44m"
MAGENTAB            = "\033[45m"
CYANB               = "\033[46m"
WHITEB              = "\033[47m"
DEFAULTB            = "\033[49m"

fgColors = {"0": BOLDOFF + BLACKF, "1": BOLDOFF + REDF, "2": BOLDOFF + GREENF, "3": BOLDOFF + YELLOWF,
            "4": BOLDOFF + BLUEF, "5": BOLDOFF + MAGENTAF, "6": BOLDOFF + CYANF, "7": BOLDOFF + WHITEF,

            "A": BOLDON + BLACKF, "B": BOLDON + REDF, "C": BOLDON + GREENF, "D": BOLDON + YELLOWF,
            "E": BOLDON + BLUEF, "F": BOLDON + MAGENTAF, "G": BOLDON + CYANF, "H": BOLDON + WHITEF}


bgColors = {"0": BLACKB, "1": REDB, "2": GREENB, "3": YELLOWB,
            "4": BLUEB, "5": MAGENTAB, "6": CYANB, "7": WHITEB}

def mapColors(strn, fgMap, bgMap, *, fCols=fgColors, bCols=bgColors):

    currentColorF = ""
    currentColorB = ""

    ret = []

    if not (len(strn) == len(fgMap) == len(bgMap) ):
        raise AssertionError("string and maps not equal lengths")


    for pos, char in enumerate(strn):
        fChar = fgMap[pos]
        bChar = bgMap[pos]

        if fChar in fCols:
            if currentColorF != fChar:
                ret.append(fCols[fChar] )
                currentColorF = fChar

        else:
            if currentColorF != "":
                ret.append(DEFAULTF + BOLDOFF)
            currentColorF = ""

        if bChar in bCols:
            if currentColorB != bChar:
                ret.append(bCols[bChar] )
                currentColorB = bChar

        else:
            if currentColorB != "":
                ret.append(DEFAULTB)
            currentColorB = ""


        ret.append(char)

    ret.append(RESET)

    return "".join(ret)

