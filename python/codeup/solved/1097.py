board = []
for _ in range(19):
    board.append(list(map(int, input().split())))
n = int(input())
positions = []
for _ in range(n):
    positions.append(list(map(int, input().split())))
while positions:
    a, b = positions.pop(0)
    #board[a-1][b-1] = 0 if board[a-1][b-1] else 1
    for i in range(19):
        board[a-1][i] = 0 if board[a-1][i] else 1
        board[i][b-1] = 0 if board[i][b-1] else 1
answer = []
for i in range(19):
    print(*board[i])
