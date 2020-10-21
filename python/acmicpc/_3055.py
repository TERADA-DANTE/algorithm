from collections import deque
h, w = list(map(int, input().split()))

board = [list(input()) for _ in range(h)]
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]


class Forest:
    def __init__(self, data):
        self.board = data
        self.waters = self.__getWaters__()
        self.start = self.__getStart__()
        self.end = self.__getEnd__()
        self.isVisited = self.__isVisited__()

    def __getWaters__(self):
        waters = deque()
        for i in range(h):
            for j in range(w):
                if self.board[i][j] == '*':
                    waters.append([i, j])
        return waters

    def __getStart__(self):
        for i in range(h):
            for j in range(w):
                if self.board[i][j] == 'S':
                    return [i, j]

    def __getEnd__(self):
        for i in range(h):
            for j in range(w):
                if self.board[i][j] == 'D':
                    return [i, j]

    def __isVisited__(self):
        temp = [[None] * w for _ in range(h)]
        for i, v in self.waters:
            temp[i][v] = True
        return temp

    def flood(self):
        newWaters = []
        while self.waters:
            r, c = self.waters.pop()
            for a, b in moves:
                row, col = r+a, c+b
                if 0 <= row < h and 0 <= col < w and not self.isVisited[row][col] and self.board[row][col] == '.':
                    self.isVisited[row][col] = True
                    self.board[row][col] = '*'
                    newWaters.append([row, col])
        self.waters = newWaters

        return self.board


def solution(board, w, h):
    forest = Forest(board)
    start = forest.start
    isVisited = [[None]*w for _ in range(h)]
    queue = deque([[0, *start]])

    end = forest.end
    isVisited[start[0]][start[1]] = True
    while queue:

        for _ in range(len(queue)):
            cnt, r, c = queue.popleft()

            if board[r][c] == '*':
                continue
            if r == end[0] and c == end[1]:
                return cnt
            for a, b, in moves:
                row, col = r+a, c+b
                if 0 <= row < h and 0 <= col < w and not isVisited[row][col] and board[row][col] in ['D', '.']:
                    isVisited[row][col] = True
                    queue.append([cnt+1, row, col])
        board = forest.flood()

    return 'KAKTUS'


print(solution(board, w, h))
