def sqaure(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a, b = input().split()
a = int(a)
b = int(b)

for i in sqaure(a, b):
    print(i)