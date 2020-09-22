n, k = list(map(int, input().split()))

numbers = list(map(int, input().split()))
l = 0
cnt = 0
s = 0
for r in range(len(numbers)):
    s += numbers[r]
    if s > k:
        while s >= k:
            s -= numbers[l]
            l += 1
            if s == k:
                cnt += 1
                break
    elif s == k:
        s -= numbers[l]
        l += 1
        cnt += 1
    else:
        pass


print(cnt)
