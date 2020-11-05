col, row = list(map(int, input().split()))
k = int(input())


def solution(col, row, k):
    board = [[0] * col for _ in range(row)]
    pos = [row-1, 0, 0]

    def next(r, c, flag):
        if flag == 0:
            if r-1 < 0 or board[r-1][c]:
                return next(r, c, (flag+1) % 4)
            return [r-1, c, flag]
        if flag == 1:
            if c+1 >= col or board[r][c+1]:
                return next(r, c, (flag+1) % 4)
            return [r, c+1, flag]
        if flag == 2:
            if r+1 >= row or board[r+1][c]:
                return next(r, c, (flag+1) % 4)
            return [r+1, c, flag]
        if flag == 3:
            if c-1 < 0 or board[r][c-1]:
                return next(r, c, (flag+1) % 4)
            return [r, c-1, flag]
    if k > row*col:
        return [0]
    for i in range(row*col):
        r, c, flag = pos
        board[r][c] = i+1
        if i+1 == k:
            return [c+1, row-r]
        pos = next(r, c, flag)


print(*solution(col, row, k))
