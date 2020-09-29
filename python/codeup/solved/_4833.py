strings = list(input())
o, c = 0, 0
a = 0
for i in range(len(strings)):
    if strings[i] == '(':
        o += 1
    else:
        c += 1
    if c:
        if strings[i-1] == '(':
            a += o-1
        else:
            a += 1
        c = 0
        o -= 1
print(a)
