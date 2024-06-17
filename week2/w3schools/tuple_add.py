thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)




thistuple1 = ("apple", "banana", "cherry")
x = ("orange",)
thistuple1 += x

print(thistuple1)