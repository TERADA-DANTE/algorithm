n = int(input())

dp = [0, 1, 3] + [None] * (n-2)

for i in range(3, n+1):
    dp[i] = (dp[i-1] + (dp[i-2]*2)) % 100007

print(dp[n] % 100007)
