from collections import deque
n, m = list(map(int, input().split()))
[board, isVisited, steps] = [[], [], [[0, 1], [-1, 0], [0, -1], [1, 0]]]

for _ in range(n):
    board += [list(map(int, list(input())))]
    isVisited += [[False]*m]


def solution(board):
    dq = deque([[0, 0]])
    isVisited[0][0] = 1
    while dq:
        [i, j] = dq.popleft()
        candidates = []
        for k, l in steps:
            [a, b] = [i+k, j+l]
            if 0 <= a < n and 0 <= b < m and board[a][b]:
                if isVisited[a][b]:
                    isVisited[a][b] = min(
                        [isVisited[i][j] + 1, isVisited[a][b]])
                else:
                    isVisited[a][b] = isVisited[i][j] + 1
                    candidates.append([a, b])
        dq += candidates
    return isVisited[-1][-1]


print(solution(board))
