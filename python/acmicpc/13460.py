from collections import deque
row, col = list(map(int, input().split()))
data = [list(input()) for _ in range(row)]


class Board:
    def __init__(self, data):
        self.board = data
        self.flag = False

    def __search__(self):
        row, col = len(self.board), len(self.board[0])
        candidates = []
        for i in range(row):
            for j in range(col):
                if self.board[i][j] in ['R', 'B']:
                    candidates.append([i, j])
        return candidates

    def getStart(self, r, c, direction):
        if direction % 2:
            offset = direction-2
            while c and c < col:
                if self.board[r][c] == '#':
                    return c
                c = c+offset
            return c
        else:
            offset = direction-1
            while r and r < row:
                if self.board[r][c] == '#':
                    return r
                r = r+offset
            return r

    def execute(self, direction):
        candidates = self.__search__()
        for i in range(len(candidates)):
            R, C = candidates[i]
            s = self.getStart(R, C, direction)
            ball = self.board[R][C]
            if direction == 0:
                offset = [self.board[s+i][C]
                          for i in range(R-s+1)].count('.')

                flag = [self.board[s+i][C] for i in range(R-s+1)].count('O')
            if direction == 1:
                offset = self.board[R][s:C].count('.')
                flag = self.board[R][s:C].count('O')
            if direction == 2:
                offset = [self.board[R+i][C]
                          for i in range(s-R+1)].count('.')
                flag = [self.board[R+i][C] for i in range(s-R+1)].count('O')
            if direction == 3:
                offset = self.board[R][C:s].count('.')
                flag = self.board[R][C:s].count('O')
            candidates[i] = [ball, R, C, offset, flag]
        for ball, r, c, offset, flag in candidates:
            if flag:
                if ball == 'R':
                    self.flag = True
                else:
                    return -1
            else:
                self.board[r][c] = '.'
                if direction == 0:
                    self.board[r-offset][c] = ball
                if direction == 1:
                    self.board[r][c-offset] = ball
                if direction == 2:
                    self.board[r+offset][c] = ball
                if direction == 3:
                    self.board[r][c-offset] = ball
        return self.flag


def solution():
    queue = deque([[Board(data), 0]])
    while queue:
        q, count = queue.popleft()
        print(q.board)
        if count < 1:
            for i in range(4):
                newBoard = Board(q.board)
                flag = newBoard.execute(i)
                if flag == True:
                    return count
                else:
                    queue.append([newBoard, count+1
                                  ])
    return -1


print(solution())
