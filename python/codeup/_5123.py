n = int(input())
numbers = list(map(int, input().split()))
factorials = [1]
dp = [0, 0, 0]


def combination(n, k):
    if not n:
        return 0
    elif n == 1:
        return 1
    return factorials[n] / (factorials[k] * factorials[n-k])


for number in numbers:
    dp[number % 3] += 1
for i in range(1, dp[0]+1):
    factorials.append(factorials[-1]*i)
print(int(combination(dp[0], 2) + dp[1]*dp[2]))
