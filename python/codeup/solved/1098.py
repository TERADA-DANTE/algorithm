h, w = list(map(int, input().split()))
board = [[0]*w for _ in range(h)]
n = int(input())
for _ in range(n):
    l, d, x, y = list(map(int, input().split()))
    if d:
        for i in range(l):
            board[x+i-1][y-1] = 1
    else:
        for i in range(l):
            board[x-1][y-1+i] = 1
for i in range(h):
    print(*board[i])
