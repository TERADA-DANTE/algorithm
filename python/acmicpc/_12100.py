from collections import deque
n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]


class Candidates:
    def __init__(self):
        self.moves = [0, 1, 2, 3]
        self.arr = []
        self.__makeCombinations__(0, [])

    def __makeCombinations__(self, cnt, history):
        if cnt == 5:
            self.arr.append(history)
            return
        for move in self.moves:
            self.__makeCombinations__(cnt+1, history+[move])


class Board:
    def __init__(self, data):
        self.board = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.board[i][j] = data[i][j]

    def execute(self, direction):
        # up
        if direction == 0:
            ret = []
            for i in range(n):
                slice = deque([v for v in [self.board[j][i]
                                           for j in range(n)] if v])
                temp = []
                while slice:
                    s = slice.popleft()
                    if s and slice and s == slice[0]:
                        s = slice.popleft()
                        temp.append(s*2)
                    else:
                        temp.append(s)
                if len(temp) < n:
                    temp += [0] * (n-len(temp))
                ret.append(temp)
            return list(map(list, zip(*ret)))
        # right
        if direction == 1:
            ret = []
            for i in range(n):
                slice = deque([v for v in self.board[i] if v])
                temp = []
                while slice:
                    s = slice.pop()
                    if s and slice and s == slice[-1]:
                        s = slice.pop()
                        temp.append(s*2)
                    else:
                        temp.append(s)
                if len(temp) < n:
                    temp += [0] * (n-len(temp))
                ret.append(list(reversed(temp)))
            return ret
        # down
        if direction == 2:
            ret = []
            for i in range(n):
                slice = deque([v for v in [self.board[j][i]
                                           for j in range(n)] if v])
                temp = []
                while slice:
                    s = slice.pop()
                    if s and slice and s == slice[-1]:
                        s = slice.pop()
                        temp.append(s*2)
                    else:
                        temp.append(s)
                if len(temp) < n:
                    temp += [0] * (n-len(temp))
                ret.append(temp)

            return list(map(list, zip(*list(map(reversed, ret)))))
        # left
        if direction == 3:
            ret = []
            for i in range(n):
                slice = deque([v for v in self.board[i] if v])
                temp = []
                while slice:
                    s = slice.popleft()
                    if s and slice and s == slice[0]:
                        s = slice.popleft()
                        temp.append(s*2)
                    else:
                        temp.append(s)
                if len(temp) < n:
                    temp += [0] * (n-len(temp))
                ret.append(temp)
            return ret


def solution():
    # 4 ** 5 = 1024
    answer = 0
    candidates = Candidates()
    for directions in candidates.arr:
        board = Board(data)

        while directions:
            direction = directions.pop()
            board = Board(board.execute(direction))
        for i in range(n):
            for j in range(n):
                answer = max(answer, board.board[i][j])
    return answer


print(solution())
