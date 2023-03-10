import re

f = open('text.txt', encoding='utf-8')
s = str(f.read())

x = re.sub(" ", ',', s)

print(x)