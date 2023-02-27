import re

#Write a Python program to convert a given camel case string to snake case.

def ToSnake(s):
    return re.sub("(?!^)(?=[A-Z])", '_', s).lower()

text = input()

res = ToSnake(text)

print(res)