import re

# Write a Python program to split a string at uppercase letters.

text = input()

match = re.split('[A-Z]', text)

print(match)
