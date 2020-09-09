n = int(input())

board = [input().split() for _ in range(n)]
cnt = dict({1: 0, 0: 0})


def half(arr, n):
    return [arr[0:n], arr[n:]]


def partition(board, n):
    return half([row[0:n] for row in board], n) + half([row[n:] for row in board], n)


def isSquare(board, n):
    global cnt
    origin = board[0][0]
    for i in range(n):
        for j in range(n):
            if board[i][j] != origin:
                return False

    cnt[int(origin)] += 1
    return True


def solution(board, n):
    if isSquare(board, n):
        return
    else:
        return [solution(board, int(n//2)) for board in partition(board, int(n//2))]


solution(board, n)
print('\n'.join(list(map(str, [cnt[0], cnt[1]]))))
