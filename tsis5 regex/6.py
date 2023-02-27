import re

#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

text = input()

match = re.sub('\s', ':', text)
match = re.sub('[.]', ':', match)
match = re.sub('[,]', ':', match)


print(match)