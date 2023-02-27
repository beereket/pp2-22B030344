import re

#Write a Python program to insert spaces between words starting with capital letters.


text = input()

match = re.split('[A-Z]', text)

for iter in match:
    print(iter, ' ')
