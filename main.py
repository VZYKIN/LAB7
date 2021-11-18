
def mergelists(obj1111, obj2222):
    if obj1111.getDate() < obj2222.getDate():
        return -1
    elif obj1111.getDate() > obj2222.getDate():
        return 1
    else:
        return 0



list = vzlist1 + vzlist2
list.sort(compareDate)
