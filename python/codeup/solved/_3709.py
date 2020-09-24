n = int(input())
dp = [0, 1, 2] + [None] * (n-2)

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 100000007
print(dp[n] % 100000007)
