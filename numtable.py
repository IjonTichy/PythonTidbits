from ansicodes import *

def equal(x, y, product):
    return x == y

def falseFunc(x, y, product):
    return False

def numTable(xmin, xmax, ymin, ymax, checkFunc=falseFunc):

    xSize = len(str(xmax*ymax)) + 2

    rowInvert = 0
    colInvert = 0

    PRINTSTR = "{{0:^{0}}}".format(xSize)

    HEADSTRING  = BOLDON + WHITEF + BLUEB + PRINTSTR    + RESET
    HEADSTRING2 = BLACKB + WHITEF + (" " * xSize)       + RESET
    BODYSTRING1 = BLACKB + WHITEF + PRINTSTR            + RESET
    BODYSTRING2 = WHITEB + BLACKF + PRINTSTR            + RESET

    BODYSTRING3 = BLACKB + REDF + BOLDON + PRINTSTR     + RESET
    BODYSTRING4 = WHITEB + REDF + BOLDON + PRINTSTR     + RESET

    for i in range(ymin-1, ymax+1):

        if i == ymin-1:
            print(HEADSTRING2, end="")
        else:
            print(HEADSTRING.format(i), end="")

    print()

    for i in range(xmin, xmax+1):

        print(HEADSTRING.format(i), end="")

        for j in range(ymin, ymax+1):

            product = i * j

            inv = rowInvert ^ colInvert

            if checkFunc(i, j, product) == True:
                if inv:
                    tmp = BODYSTRING3
                else:
                    tmp = BODYSTRING4
            else:
                if inv:
                    tmp = BODYSTRING1
                else:
                    tmp = BODYSTRING2


            colInvert = not colInvert
            print(tmp.format(product), end="")

        print()
        rowInvert = not rowInvert
        colInvert = 0


    print()
