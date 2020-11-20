n = int(input())
cnt = 0
while n:
    t = 1
    while t <= n:
        t *= 2
    n -= int(t/2)
    cnt += 1
print(cnt)
