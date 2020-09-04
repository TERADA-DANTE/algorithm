n = int(input())


def solution(n):
    dp = [0, 1, 2, 3, 5]
    for i in range(5, n+1):
        dp.append((dp[i-1] + dp[i-2]) % 15746)
    return dp[n] % 15746


print(solution(n))
