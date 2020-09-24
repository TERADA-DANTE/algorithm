n = int(input())

dp = [1, 1, 2] + [None] * (n-2)

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]*3) % 1000

print(dp[n] % 1000)
