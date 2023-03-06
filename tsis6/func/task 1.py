import functools

n = int(input())
a = input().split()

for i in range(0, n, 1):
    a[i] = int(a[i])

ans = functools.reduce((lambda x, y: x * y), a)
print(ans)