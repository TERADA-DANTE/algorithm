a, b = list(map(int, input().split()))
if a > b:
    a, b = b, a
cnt = 0

while a < b:
    d = b-a
    if 8 <= d:
        cnt += 1
        a += 10
    elif 4 <= d <= 7:
        cnt += 1
        a += 5
    else:
        cnt += 1
        a += 1
if a == b:
    print(cnt)
else:
    print(cnt+abs(a-b))
