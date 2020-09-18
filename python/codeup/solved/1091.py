a, m, d, n = list(map(int, input().split()))

dp = [None] + [a] + [None] * 10001203
for i in range(2, n+1):
    dp[i] = dp[i-1]*m + d
print(dp[n])
