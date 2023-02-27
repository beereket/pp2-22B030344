import re

#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

text = input()

pattern = r'a.*b'
match = re.search(pattern, text)

print(match.group())