""""""
def filterArray(arr):
    """"""
    setArr = set(arr)
    for e in setArr:
        while arr.count(e) > 1:
            arr.remove(e)
        if type(e) == str:
            arr.remove(e)
    return arr


