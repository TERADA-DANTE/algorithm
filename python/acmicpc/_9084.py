answer = []


def solution(n, money, m):
    dp = [[1] + [0] * m for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if j < money[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-money[i]]
    return dp[-1][-1]


for _ in range(int(input())):
    n = int(input())
    money = list(map(int, input().split()))
    m = int(input())
    answer.append(solution(n, [None] + money, m))

print('\n'.join(list(map(str, answer))))
