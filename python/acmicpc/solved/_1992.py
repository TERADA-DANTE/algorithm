n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, list(input()))))


def isZipable(board, m):
    origin = board[0][0]
    for row in range(m):
        for col in range(m):
            if board[row][col] != origin:
                return False
    return True


def partition(board, row, col, n):
    part = []
    for i in range(n):
        part.append(board[row+i][col:col+n])
    return part


def solution(board, n):
    if isZipable(board, n):
        return board[0][0]
    return [solution(partition(board, row, col, n//2), n//2) for row, col in [[0, 0], [0, n//2], [n//2, 0], [n//2, n//2]]]


print(str(solution(board, n)).replace(
    ', ', '').replace('[', '(').replace(']', ')'))
