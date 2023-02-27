import re

#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

get = open('row.txt', encoding='utf-8')
text = str(get.read())

pattern = r'ab{2, 3}$'
match = re.search(pattern, text)

print(match.group())