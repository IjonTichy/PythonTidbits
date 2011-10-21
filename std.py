#!/usr/bin/python3

import math
import random
import collections

def mean(seq):
    "Get the mean of a sequence of numbers"
    return sum(seq) / len(seq)

def std(seq):
    "Get the standard deviation of a sequence of numbers"
    mean_ = mean(seq)
    length = len(seq)

    deviations = []

    ret = 0

    for i in seq:
        deviations.append( (i - mean_) ** 2)

    return math.sqrt(sum(deviations) / length)

def deviations(seq):
    "Tells you the percentage of numbers x standard deviations away from the mean"

    dev = collections.defaultdict(list)
    ret = collections.defaultdict(int)

    mean_ = mean(seq)
    std_ =  std(seq)
    len_ = len(seq)

    for i in seq:

        away = math.ceil(abs(i - mean_) / std_ )
        dev[away].append(i)

    last = []

    for i in sorted(dev):
        current = last + dev[i]
        dev[i] = current
        last = current

        ret[i] = len(dev[i]) / len_

    return dict(dev), dict(ret)

def percWithin(seq, lo=None, hi=None):
    "Returns the numbers in the sequence within the range specified"

    ret  = []
    len_ = len(seq)

    for i in seq:

        if lo is None and hi is None:
            ret.append(i)

        elif lo is None:
            if i <= hi:
                ret.append(i)

        elif hi is None:
            if i >= lo:
                ret.append(i)

        else:
            if lo <= i <= hi:
                ret.append(i)


    return len(ret) / len_


def shoot(damage, count):
    "Fire a Doom hitscan shot"
    ret = 0

    for i in range(count):
        ret += damage * random.randint(1, 3)

    return ret

def proj(damage, count):
    "Roll for Doom projectile damage"
    ret = 0

    for i in range(count):
        ret += damage * random.randint(1, 8)

    return ret

def seqMany(func, amount, *a, **ka):
    "Do <func> <amount> times and return the results"
    ret = []

    for i in range(amount):
        ret.append(func(*a, **ka) )

    return ret
