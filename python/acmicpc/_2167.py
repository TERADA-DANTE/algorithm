n, m = list(map(int, input().split()))


def solution(n, m):
    board = [[0] * m] + [[0] +
                         list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * (m+1) for _ in range(n+1)]
    answer = []
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + board[i][j] - dp[i-1][j-1]
    for _ in range(int(input())):
        i, j, x, y = list(map(int, input().split()))
        answer.append(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])
    return '\n'.join(list(map(str, answer)))


print(solution(n, m))
