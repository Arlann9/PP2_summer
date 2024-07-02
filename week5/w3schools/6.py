import re
txt = input()
x = re.sub('[ .,]', ':', txt, 4)
print(x)