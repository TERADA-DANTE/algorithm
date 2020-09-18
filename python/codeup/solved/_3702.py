r, c = list(map(int, input().split()))
dp = [1] * c
for _ in range(r-1):
    for i in range(c):
        dp[i] = 1 if not i else (dp[i-1] + dp[i]) % 100000000
print(dp[c-1])
