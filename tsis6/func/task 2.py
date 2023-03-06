s = str(input())

cnt_upper = 0
cnt_lower = 0

for i in s:
    if i.isupper():
        cnt_upper += 1
    elif i.islower():
        cnt_lower += 1

print(cnt_upper)
print(cnt_lower)