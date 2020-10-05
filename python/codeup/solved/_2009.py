k, n = list(map(int, input().split()))
cnt = 0
while k >= n:
    cnt += int(k//n)
    k = k % n + int(k//n)
print(cnt)
