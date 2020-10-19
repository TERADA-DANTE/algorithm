from collections import deque
row, col = list(map(int, input().split()))


def solution(row, col):
    board = [list(map(int, list(input()))) for _ in range(row)]
    answer = float('inf')
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    isVisited = [[float('inf')] * col for _ in range(row)]
    isVisited[0][0] = 0
    queue = deque([[0, 0, 0, 0]])
    while queue:
        r, c, isPassed, cnt = queue.popleft()
        if r == row-1 and c == col-1:
            answer = min(answer, cnt)
            continue
        for a, b in moves:
            x, y = r+a, c+b
            if 0 <= x < row and 0 <= y < col:
                # 벽을 부쉈다면 벽이 있는 곳은 갈 수 없다.
                # 벽을 부수지 않았다면 최단 거리라면 갈 수있다.
                if isPassed:
                    if not board[x][y] and isVisited[x][y] > isVisited[r][c]+1:
                        isVisited[x][y] = isVisited[r][c]*1000
                        queue.append([x, y, 1, cnt+1])
                else:
                    if isVisited[x][y] > isVisited[r][c] + 1:
                        isVisited[x][y] = isVisited[r][c] + 1
                        queue.append([x, y, 1 if board[x][y] else 0, cnt+1])
    return -1 if answer == float('inf') else answer + 1


print(solution(row, col))
