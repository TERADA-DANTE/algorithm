n = int(input())
dp = [1, 2, 7] + [None] * (n-2)
dp2 = [1, 3, 10] + [None] * (n-2)
for i in range(3, n+1):
    dp[i] = (dp2[i-1]*2+dp[i-2]) % 100007
    dp2[i] = (dp[i] + dp2[i-1]) % 100007

print(dp[n] % 100007)
