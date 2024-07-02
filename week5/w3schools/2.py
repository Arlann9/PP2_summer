import re
txt = input()
match = re.search( 'a(b{2,3})', txt)
if match:
    print("ok")
else:
    print("no")