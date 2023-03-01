import re

#Write a Python program to find sequences of lowercase letters joined with a underscore.

text = input()


pattern = r'[a-z]+_*[a-z]+'
match = re.search(pattern, text)

print(match.group())
