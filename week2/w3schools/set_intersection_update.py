set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)



set4 = {"apple", 1,  "banana", 0, "cherry"}
set5 = {False, "google", 1, "apple", 2, True}

set6 = set4.intersection(set5)

print(set6)