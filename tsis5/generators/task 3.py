n = int(input())

a = [i for i in range(0, n + 1, 1) if i % 3 == 0 and i % 4 == 0]

print(a)
