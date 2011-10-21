#!/usr/bin/env python3

from collections import Iterable
import sys

__all__ = ['doublePreceding', 'doubleSucceeding', 'testDoubles']

testList = [9, 4, 3]

def doublePreceding(vals):

    failure = None

    try:
        prev = 0

        for val in vals:
            yield prev*2
            prev = val
    except TypeError as e:
        excReason = str(sys.exc_info()[1])

        if 'subscriptable' in excReason or 'iterable' in excReason:
            valsType  = vals.__class__.__name__
            failure = TypeError("cannot iterate over {0}".format(valsType) )

        elif 'for *' in excReason:
            valType  = val .__class__.__name__
            prevType = prev.__class__.__name__
            failure = TypeError("cannot multiply {0} by {1}".format(valType, prevType) )

        else:
            failure = TypeError("unknown type error")

    if failure:
        raise failure


def doubleSucceeding(vals):

    failure = None

    try:
        next = vals[1]

        for i, val in enumerate(vals):
            yield next*2
            try:
                next = vals[i+2]
            except IndexError:
                yield 0
                break
    except TypeError as e:
        excReason = str(sys.exc_info()[1])

        if 'subscriptable' in excReason or 'iterable' in excReason:
            valsType  = vals.__class__.__name__
            failure = TypeError("cannot iterate over {0}".format(valsType) )

        elif 'for *' in excReason:
            valType  = val .__class__.__name__
            nextType = next.__class__.__name__
            failure = TypeError("cannot multiply {0} by {1}".format(valType, nextType) )

        else:
            failure = TypeError("unknown error")

    if failure:
        raise failure

def testDoubles():
    print(testList)
    print(list(doublePreceding(testList) ) )
    print(list(doubleSucceeding(testList) ) )
