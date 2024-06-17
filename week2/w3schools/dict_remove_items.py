thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1.pop("model")
print(thisdict1)

thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2.popitem()
print(thisdict2)


thisdict3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict3["model"]
print(thisdict3)

thisdict4 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict4.clear()
print(thisdict4)