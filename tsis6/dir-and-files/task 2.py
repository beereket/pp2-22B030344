import os

s = str(input("Path: "))

if os.access(s, os.R_OK):
    print("You have read access")
else:
    print("You do not have read access")