import re
txt = input()
result = re.split(r'(?=[A-Z])', txt)
print(result)