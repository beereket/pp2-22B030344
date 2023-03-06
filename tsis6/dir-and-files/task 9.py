s = str(input("File name: "))

fileread = open(s, "r")

s1 = str(input("New file name: "))
filewrite = open(s1, "w")
filewrite.write(fileread.read())