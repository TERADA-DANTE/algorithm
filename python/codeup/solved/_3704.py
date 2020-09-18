dp = [1, 2, 4]
n = int(input())
for _ in range(n-3):
    dp.append(sum([dp[-1], dp[-2], dp[-3]]) % 1000)
print(dp[n-1])
