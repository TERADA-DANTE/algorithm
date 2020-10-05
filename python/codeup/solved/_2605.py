from collections import deque
board = [list(map(int, input().split())) for _ in range(7)]
isVisited = [[None] * 7 for _ in range(7)]
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs(i, j, color, cnt=1):
    global board, isVisited
    queue = deque([[i, j]])
    while queue:
        row, col = queue.popleft()
        isVisited[row][col] = True
        for x, y in moves:
            if 0 <= row+x < 7 and 0 <= col+y < 7:
                if not isVisited[row+x][col+y] and color == board[row+x][col+y]:
                    queue.append([row+x, col+y])
                    cnt += 1
    return cnt


acc = 0
for i in range(7):
    for j in range(7):
        if not isVisited[i][j]:
            cnt = bfs(i, j, board[i][j])
            if cnt >= 3:
                acc += 1


print(acc)
# 각점에서 dfs 실행하여 히스토리에 저장하고.
# 히스토리의 개수가 다 찼을 때 3개 이상이면
# 해당 요소를 모두 0으로 바꾼뒤 1을 증가시킨다.
