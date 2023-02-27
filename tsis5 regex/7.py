import re

#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

text = input()

match = re.split('_', text)

for iter in match:
    print(iter, sep = '')
