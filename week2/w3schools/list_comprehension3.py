#newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]


#Condition
newlist1 = [x for x in fruits if x != "apple"]
print(newlist1)

newlist2 = [x for x in fruits]
print(newlist2)


#Iterable
newlist3 = [x for x in range(10)]
print(newlist3)

newlist4 = [x for x in range(10) if x < 5]
print(newlist4)


#Expression
newlist5 = [x.upper() for x in fruits]
print(newlist5)

newlist6 = ['hello' for x in fruits]
print(newlist6)

newlist7 = [x if x != "banana" else "orange" for x in fruits]
print(newlist7)
