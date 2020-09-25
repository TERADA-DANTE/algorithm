board = [list(map(int, input().split())) for _ in range(9)]
initialValue = 0
initialIndex = 0
for i in range(9):
    for j in range(9):
        if initialValue < board[i][j]:
            initialValue = board[i][j]
            initialIndex = [i+1, j+1]
print(initialValue)
print(*initialIndex)
