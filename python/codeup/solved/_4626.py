n = int(input())
results = list(map(int, input().split()))
dp = [None] * n
for i in range(n):
    if not i:
        dp[i] = 1 if results[i] else 0
    else:
        dp[i] = 0 if not results[i] else dp[i-1]+1

print(sum(dp))
