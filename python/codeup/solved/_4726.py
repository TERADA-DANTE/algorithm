n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))
dp = [sum(numbers[0:k])]
l, r = 0, k
while r < n:
    dp.append(dp[-1]+numbers[r]-numbers[l])
    r += 1
    l += 1
print(max(dp))
