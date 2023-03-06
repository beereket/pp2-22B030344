import os

s = str(input("Path: "))

if os.path.exists(s):
    print("Path exists")
else:
    print("Path does not exist")