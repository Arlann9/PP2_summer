def myFunc(n):
    return abs(n-50)

thislist = [100,50,82,63,21]
thislist.sort(key=myFunc)
print(thislist)