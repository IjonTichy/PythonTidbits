def flatten(listToFlatten):
    for item in listToFlatten:
        if isinstance(item, (tuple, list, set)):
            for item2 in flatten(item):
                yield item2
        else:
            yield item
