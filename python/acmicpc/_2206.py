from heapq import heappop, heappush
from collections import deque
row, col = list(map(int, input().split()))


def solution(row, col):
    board = [list(map(int, list(input()))) for _ in range(row)]
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    isVisited = [[[None, None] for _ in range(col)] for _ in range(row)]
    queue = [[0, 0, 0, 0]]
    isVisited[0][0][0] = isVisited[0][0][1] = True
    while queue:
        cnt, r, c, isPassed = heappop(queue)
        if r == row-1 and c == col-1:
            return cnt+1
        for a, b in moves:
            x, y = r+a, c+b
            if 0 <= x < row and 0 <= y < col and not isVisited[x][y][isPassed]:
                if (isPassed and not board[x][y]) or not isPassed:
                    isVisited[x][y][isPassed] = True
                    heappush(
                        queue, (cnt+1, x, y, 1 if board[x][y] or isPassed else 0))

    return -1


print(solution(row, col))
