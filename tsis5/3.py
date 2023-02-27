import re

#Write a Python program to find sequences of lowercase letters joined with a underscore.

get = open('row.txt', encoding='utf-8')
text = str(get.read())


pattern = r'[a-z]+_*[a-z]+'
match = re.search(pattern, text)

print(match.group())