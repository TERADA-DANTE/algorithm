board = [list(map(int, input().split())) for _ in range(5)]

numbers = []
for _ in range(5):
    numbers += list(map(int, input().split()))
d = dict()
for i in range(5):
    for j in range(5):
        d[board[i][j]] = [i, j]


def isBingo(board):
    result = 0
    # 가로
    for i in range(5):
        if not any(board[i]):
            result += 1
    # 세로
    temp = list(map(list, zip(*board)))
    for i in range(5):
        if not any(temp[i]):
            result += 1
    # 대각
    temp = []
    for i in range(5):
        temp.append(board[i][i])
    if not any(temp):
        result += 1
    temp = []
    for i in range(5):
        temp.append(board[i][4-i])
    if not any(temp):
        result += 1

    if result >= 3:
        return True
    return False


def solution(board, numbers):
    for i in range(len(numbers)):
        row, col = d[numbers[i]]
        board[row][col] = 0
        if isBingo(board):
            return i+1


print(solution(board, numbers))
