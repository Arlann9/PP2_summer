import re
txt = input()
match = re.search('a.*b', txt)
print(match)