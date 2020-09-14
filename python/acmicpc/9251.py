
a = input()
b = input()


def initialize(a, b):
    initial = [[None] * len(a) for _ in range(len(b))]
    initial[0][0] = 1 if a[0] == b[0] else 0
    for i in range(1, len(a)):
        initial[0][i] = 1 if a[i] == b[0] else initial[0][i-1]
    for i in range(1, len(b)):
        initial[i][0] = 1 if b[i] == a[0] else initial[i-1][0]
    return initial


def solution(a, b):
    dp = initialize(a, b)
    for i in range(1, len(b)):
        for j in range(1, len(a)):
            if a[j] == b[i]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max([dp[i-1][j], dp[i][j-1]])
    return dp[-1][-1]


print(solution(a, b))
