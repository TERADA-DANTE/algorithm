from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
inf = float('inf')


def DFS(i, h, v):
    global inf
    candidates = [idx for idx, val in enumerate(
        board[i]) if val and idx not in h]
    if not candidates:
        if len(h) == n and board[h[-1]][h[0]]:
            t = v + board[h[-1]][h[0]]
            if inf > t:
                inf = t
            return
        return
    for c in candidates:
        DFS(c, h + [c], v + board[i][c])


def solution(board):
    for i in range(n):
        DFS(i, [i], 0)
    return inf


print(solution(board))
