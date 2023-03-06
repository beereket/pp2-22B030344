s = str(input("File name: "))
file = open(s, "w")

a = input().split()

for i in a:
    file.write(i + ' ')