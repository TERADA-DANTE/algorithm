n = int(input())


def solution(n):
    dp = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
          55, 89, 144, 233, 377, 610, 987, 1597]
    for i in range(18, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]


print(solution(n))
