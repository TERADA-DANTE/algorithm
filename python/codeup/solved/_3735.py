n = int(input())
numbers = list(map(int, input().split()))

dp = [1]
for i in range(1, n):
    candidates = []
    index = i
    while index:
        if numbers[index-1] < numbers[i]:
            candidates.append(dp[index-1])
        index -= 1
    if candidates:
        dp.append(max(candidates)+1)
    else:
        dp.append(1)
print(max(dp))
