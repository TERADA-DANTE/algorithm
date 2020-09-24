n = int(input())
dp = [0, 0, 0, 2] + [None] * (n-3)

for i in range(4, n+1):
    if not i % 3:
        dp[i] = (dp[i-3] * 2) % 100000007
    else:
        dp[i] = 0
print(dp[n] % 100000007)
