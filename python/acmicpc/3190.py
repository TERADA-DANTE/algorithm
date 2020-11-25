from collections import deque
n = int(input())
k = int(input())
# need offset
apples = [[None] * n for _ in range(n)]
for _ in range(k):
    row, col = list(map(int, input().split()))
    apples[row-1][col-1] = True


l = int(input())
moves = [input().split() for _ in range(l)]
# row,col, dir


class Snake:
    def __init__(self):
        self.pos = [0, 0]
        self.dir = 1
        self.body = deque([[0, 0]])
        self.time = 0

    def count(self):
        self.time += 1

    def move(self):
        row, col = self.pos
        dir = self.dir
        if dir == 0:
            row -= 1
        elif dir == 1:
            col += 1
        elif dir == 2:
            row += 1
        elif dir == 3:
            col -= 1
        return row, col


def handling(snake, isHandle):
    if snake.dir == 0:
        if isHandle == 'L':
            return 3
        else:
            return 1
    elif snake.dir == 1:
        if isHandle == 'L':
            return 0
        else:
            return 2
    elif snake.dir == 2:
        if isHandle == 'L':
            return 1
        else:
            return 3
    elif snake.dir == 3:
        if isHandle == 'L':
            return 2
        else:
            return 0


def solution():
    snake = Snake()
    while True:
        # 일단 이동
        nextRow, nextCol = snake.move()
        snake.count()
        # 벽에 부딛힘
        if not 0 <= nextRow < n or not 0 <= nextCol < n:
            return snake.time
        # 몸에 부딪힘
        for r, c in snake.body:
            if r == nextRow and c == nextCol:
                return snake.time
        # 해당 시간에 방향을 꺾는지
        isHandle = find(snake.time)
        if isHandle:
            snake.dir = handling(snake, isHandle)
        # 해당 시간에 사과를 먹는지
        isApple = False
        if apples[nextRow][nextCol]:
            isApple = True
            apples[nextRow][nextCol] = None
        # 이동 등록
        snake.body.append([nextRow, nextCol])
        if not isApple:
            snake.body.popleft()
        snake.pos = [nextRow, nextCol]

# Binary search...


def find(t):
    for i in range(l):
        time, handle = moves[i]
        if int(time) == t:
            return handle
        elif int(time) > t:
            return False


print(solution())
