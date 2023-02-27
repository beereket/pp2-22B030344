import re

# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

text = input()

pattern = r'[A-Z][a-z]+'
match = re.search(pattern, text)

print(match.group())