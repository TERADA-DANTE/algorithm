import sys
input = sys.stdin.readline
n = int(input())
board = [None] * n
for i in range(n):
    board[i] = list(map(int, input().split()))
d = {
    -1: 0,
    0: 0,
    1: 0
}


def isSquare(board, m):
    global d
    origin = board[0][0]
    for row in range(m):
        for col in range(m):
            if board[row][col] != origin:
                return False
    d[origin] += 1
    return True


def partition(arr, row, col, n):
    result = []
    for i in range(n):
        result.append(arr[row+i][col:col+n])
    return result


def solution(board, n):
    global d
    if isSquare(board, n):
        return d
    else:
        return [solution(partition(board, row, col, n//3), n//3) for row, col in [[0, 0], [0, n//3], [0, 2*n//3],
                                                                                  [n//3, 0], [n//3, n //
                                                                                              3], [n//3, 2*n//3],
                                                                                  [2*n//3, 0], [2*n//3, n//3], [2*n//3, 2*n//3]]]


solution(board, n)
print('\n'.join(map(str, list(d.values()))))
