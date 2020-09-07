n, lim = list(map(int, input().split()))
weights = [None]
values = [None]
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
data.sort(key=lambda v: v[0])


def solution(n, lim):
    weights = [None] + [data[i][0] for i in range(n)]
    values = [None] + [data[i][1] for i in range(n)]
    dp = [[0] * (lim+1)] + [[0]*(lim+1) for _ in range(n)]
    for i in range(1, n+1):
        [weight, value] = [weights[i], values[i]]
        for j in range(1, lim+1):
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight]
                           )if weight <= j else dp[i-1][j]
    return dp[-1][-1]


print(solution(n, lim))
