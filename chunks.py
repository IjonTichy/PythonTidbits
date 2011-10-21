#!/bin/python3

__all__ = ("chunks", )


def chunks(iterator, size, mapFunc=None, pad=None):
    """\
Takes an iterator, maps each item it gives with the supplied function,
and and splits it into the specified chunk sizes. Yields lists of the
specified chunk sizes until it empties out."""

    tmp = []

    for i, item in enumerate(iterator):
        if mapFunc:
            item = mapFunc(item)

        tmp.append(item)

        if i % size == size - 1:
            yield tmp
            tmp = []

    if pad:
        padAmount = size - len(tmp)

        tmp.extend([pad] * padAmount)

    yield tmp # dump the remainder
