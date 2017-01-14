list_cleaner(p):
    count = 0
    outlist = []
    for item in p:
        if isinstance(item, list) and len(item) > 0:
            outlist.append(item)
            p.remove(item)
            count = len(p)
    return outlist, count
