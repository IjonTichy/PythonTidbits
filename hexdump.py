#!/usr/bin/env python3

import chunks
from string import printable


def intToHex(number, hexLength=0):

    hexNum = hex(number)[2:].upper()
    lpad   = max(0, hexLength - len(hexNum))

    ret = ("0"*lpad) + hexNum

    return ret


def hexDump(source, size=8):

    for chunkNum, chunk in enumerate(chunks.chunks(source, size, None, -1)):

        address = "0x" + intToHex(chunkNum*size, 8)
        hexChars = []
        strChars = []

        for byte in chunk:

            if byte == -1: # padding

                hexChars.append("  ")
                strChars.append(" ")
            else:
                hexChars.append(intToHex(byte, 2))

                strChar = chr(byte)

                if strChar in "\r\n\x0C":
                    strChars.append("N")
                elif strChar in "\t\v":
                    strChars.append("T")
                elif strChar in printable:
                    strChars.append(strChar)
                else:
                    strChars.append(".")

        yield (address, hexChars, strChars)


def formatDump(source, size=8):

    yld = ""

    for address, hexChars, strChars in hexDump(source, size):

        yld = "{0}: {1}    {2}".format(address, " ".join(hexChars), "".join(strChars))

        yield yld

if __name__ == "__main__":
    import sys

    source = open(sys.argv[1], "rb")
    dump   = source.read()

    if len(sys.argv) > 2:
        size = round(float(sys.argv[2]))
    else:
        size = 8

    for line in formatDump(dump, size):
        print(line)
