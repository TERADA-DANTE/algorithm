n = int(input())

dp = [1, 1, 5] + [None] * (n-2)

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]*4 + dp[i-3]*2) % 100007

print(dp[n] % 100007)
