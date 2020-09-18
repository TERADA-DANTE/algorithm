n = int(input())

numbers = [int(input()) for _ in range(n)]

dp = [None] * n
dp[0] = numbers[0]
dp[1] = numbers[1] + numbers[0]
dp[2] = numbers[2] + max(numbers[0], numbers[1])
for i in range(3, n):
    dp[i] = max(numbers[i] + numbers[i-1] + dp[i-3], numbers[i] + dp[i-2])
print(dp[-1])
