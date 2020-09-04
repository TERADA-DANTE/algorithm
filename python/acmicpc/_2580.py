board = [list(map(int, input().split())) for _ in range(9)]
zero = [[i, j] for i in range(9) for j in range(9) if not board[i][j]]
flag = False
answer = []


def getCandidates(row, col):
    hor = board[row]
    ver = [board[i][col] for i in range(9)]
    box = []
    for i in range(3):
        for j in range(3):
            box.append(board[3*(row//3)+i][3*(col//3)+j])
    return [i for i in range(10) if i not in set(hor+ver+box)]


def solution(i):
    global flag
    if flag:
        return
    if i == len(zero):
        flag = True
        for i in range(9):
            answer.append(board[i].copy())
        return
    else:
        row, col = zero[i]
        candidates = getCandidates(row, col)
        for candidate in candidates:
            board[row][col] = candidate
            solution(i+1)
            board[row][col] = 0


solution(0)
print('\n'.join([' '.join(list(map(str, s))) for s in answer]))
