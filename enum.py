#!/usr/bin/env python3

def enum(start, inc):
    i = start

    while True:
        yield i
        i += inc
