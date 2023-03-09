import re

s = input()

pattern = r'ab*'
m = re.search(pattern, s)

print(m.group)
