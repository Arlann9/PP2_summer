thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)


thistuple1 = ("apple", "banana", "cherry")
del thistuple1
print(thistuple1) #this will raise an error because the tuple no longer exists