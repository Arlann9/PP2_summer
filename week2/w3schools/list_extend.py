thislist = ["apple", "banana", "cherry"]
tropical = ["mango","pineapple","papaya"]
#u can add any iterable object(tuple,sets,etc)
thistuple = ("kiwi","orange")
thislist.extend(tropical)
print(thislist)
thislist.extend(thistuple)
print(thislist)