n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def solution(n, board):
    for i in range(n):
        for j in range(n):
            if board[i][j]:


print(solution(n, board))
