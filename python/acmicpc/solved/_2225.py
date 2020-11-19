import math
n, k = list(map(int, input().split()))

# DP!!


def solution(n, k):
    dp = [[None] * (n+1) for _ in range(k+1)]
    for i in range(k+1):
        for j in range(n+1):
            if not i:
                dp[i][j] = 0
            elif not j:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000
    return dp[-1][-1] % 1000000000


print(solution(n, k))
# 002


# 101
# 011

# 020
# 110
# 200
