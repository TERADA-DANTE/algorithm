board = [list(map(int, input().split())) for _ in range(9)]
r, c = list(map(int, input().split()))
if board[r-1][c-1]:
    print(-1)
else:
    cnt = 0
    for i in range(3):
        for j in range(3):
            row = r-2+i
            col = c-2+j
            if 0 <= row < 9 and 0 <= col < 9:
                if board[row][col]:
                    cnt += 1
    print(cnt)
