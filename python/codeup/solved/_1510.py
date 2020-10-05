n = int(input())
board = [[None] * n for _ in range(n)]

# 1. 시작은 첫 행, 한 가운데 열에 1을 둔다.


# 2. 행을 감소, 열을 증가하면서 순차적으로 수를 넣어간다.
row = 0
col = int(n//2)
cnt = 1
while not isinstance(board[row][col], int):
    board[row][col] = cnt
    if not cnt % n:
        row = (row+1) % n
    else:
        row = row-1 if row - 1 >= 0 else row - 1 + n
        col = (col+1) % n
    cnt += 1
for i in range(n):
    print(*board[i])
# 3. 행은 감소하므로 첫 행보다 작아지는 경우에는 마지막 행으로 넘어간다.

# 4. 열은 증가하므로 마지막 열보다 커지는 경우에는 첫 열로 넘어간다.

# 5. 넣은 수가 n의 배수이면 행만 증가한다. 열은 변화없음.
