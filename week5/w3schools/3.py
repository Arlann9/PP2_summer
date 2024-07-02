import re
txt = input()
match = re.findall("[a-z]+\_+[a-z]", txt)
if match:
    print("Match")
else:
    print("No match")