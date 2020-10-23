n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')


def solution(n, board):
    dp = [[None] * (2**n+1) for _ in range(n+1)]

    def execute(v=1, e=1 << 0):
        global answer
        if e == (1 << n) - 1:
            if board[v-1][0]:
                return board[v-1][0]
            return float('inf')
        if dp[v][e]:
            return dp[v][e]
        for i in range(n):
            if (1 << i & e) == 0 and board[v-1][i]:
                dp[v][e] = min(dp[v][e], execute(
                    i+1, i << i | e) + board[v][i+1])

    execute()
    return answer


print(solution(n, board))
