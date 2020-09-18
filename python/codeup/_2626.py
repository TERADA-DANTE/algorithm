n = int(input())
cnt = 0
for i in range(1, int(n//3)+1):
    a = i
    r = n - i
    for j in range(i, int(r//2)+1):
        b = j
        c = r - j
        if a+b > c:
            cnt += 1
print(cnt)
