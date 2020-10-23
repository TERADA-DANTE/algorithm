r, c = list(map(int, input().split()))

board = [input() for _ in range(r)]


def isSquare(i, j, size):
    for k in range(int((size-1)//2)+1):
        for l in range(size):
            if board[i+k][j+l] != board[size+i-k-1][size+j-l-1]:
                return False
    return True


def solution(r, c, board):
    l = min(r, c)
    for size in range(l, 1, -1):
        for i in range(r-size+1):
            for j in range(c-size+1):
                if isSquare(i, j, size):
                    return size
    return 1


print(solution(r, c, board))
