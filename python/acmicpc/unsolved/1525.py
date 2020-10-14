from collections import deque
board = [list(map(int, input().split())) for _ in range(3)]


def exchange(a, b, x, y, board):
    newBoard = [board[i].copy() for i in range(3)]
    newBoard[a][b], newBoard[x][y] = newBoard[x][y], newBoard[a][b]
    return newBoard


def isSame(a, b):
    for i in range(3):
        for j in range(3):
            if a[i][j] != b[i][j]:
                return False
    return True


def findZero(board):
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                return [i, j]


def solution(board):
    candidates = []
    dq = deque([(0, findZero(board), board)])
    isVisited = dict()
    while dq:
        c, [row, col], b = dq.popleft()
        candidates.append((c, b))
        if row == 0 and col == 0:
            if not isVisited.get('0001'):
                isVisited['0100'] = True
                dq.append((c+1, [0, 1], exchange(row, col, 0, 1, b)))
            if not isVisited.get('0010'):
                isVisited['1000'] = True
                dq.append((c+1, [1, 0], exchange(row, col, 1, 0, b)))

        elif row == 0 and col == 1:
            if not isVisited.get('0100'):
                isVisited['0001'] = True
                dq.append((c+1, [0, 0], exchange(row, col, 0, 0, b)))
            if not isVisited.get('0102'):
                isVisited['0201'] = True
                dq.append((c+1, [0, 2], exchange(row, col, 0, 2, b)))
            if not isVisited.get('0111'):
                isVisited['1101'] = True
                dq.append((c+1, [1, 1], exchange(row, col, 1, 1, b)))
        elif row == 0 and col == 2:
            if not isVisited.get('0201'):
                isVisited['0102'] = True
                dq.append((c+1, [0, 1], exchange(row, col, 0, 1, b)))
            if not isVisited.get('0212'):
                isVisited['1202'] = True
                dq.append((c+1, [1, 2], exchange(row, col, 1, 2, b)))
        elif row == 1 and col == 0:
            if not isVisited.get('1000'):
                isVisited['0010'] = True
                dq.append((c+1, [0, 0], exchange(row, col, 0, 0, b)))
            if not isVisited.get('1011'):
                isVisited['1110'] = True
                dq.append((c+1, [1, 1], exchange(row, col, 1, 1, b)))
            if not isVisited.get('1020'):
                isVisited['2010'] = True
                dq.append((c+1, [2, 0], exchange(row, col, 2, 0, b)))
        elif row == 1 and col == 1:
            if not isVisited.get('1112'):
                isVisited['1211'] = True
                dq.append((c+1, [1, 2], exchange(row, col, 1, 2, b)))
            if not isVisited.get('1110'):
                isVisited['1011'] = True
                dq.append((c+1, [1, 0], exchange(row, col, 1, 0, b)))
            if not isVisited.get('1101'):
                isVisited['0111'] = True
                dq.append((c+1, [0, 1], exchange(row, col, 0, 1, b)))
            if not isVisited.get('1121'):
                isVisited['2111'] = True
                dq.append((c+1, [2, 1], exchange(row, col, 2, 1, b)))
        elif row == 1 and col == 2:
            if not isVisited.get('1222'):
                isVisited['2212'] = True
                dq.append((c+1, [2, 2], exchange(row, col, 2, 2, b)))
            if not isVisited.get('1211'):
                isVisited['1112'] = True
                dq.append((c+1, [1, 1], exchange(row, col, 1, 1, b)))
            if not isVisited.get('1202'):
                isVisited['0212'] = True
                dq.append((c+1, [0, 2], exchange(row, col, 0, 2, b)))
        elif row == 2 and col == 0:
            if not isVisited.get('2010'):
                isVisited['1020'] = True
                dq.append((c+1, [1, 0], exchange(row, col, 1, 0, b)))
            if not isVisited.get('2021'):
                isVisited['2120'] = True
                dq.append((c+1, [2, 1], exchange(row, col, 2, 1, b)))
        elif row == 2 and col == 1:
            if not isVisited.get('2122'):
                isVisited['2221'] = True
                dq.append((c+1, [2, 2], exchange(row, col, 2, 2, b)))
            if not isVisited.get('2111'):
                isVisited['1121'] = True
                dq.append((c+1, [1, 1], exchange(row, col, 1, 1, b)))
            if not isVisited.get('2120'):
                isVisited['2021'] = True
                dq.append((c+1, [2, 0], exchange(row, col, 2, 0, b)))
        elif row == 2 and col == 2:
            isVisited['1222'] = True
            dq.append((c+1, [1, 2], exchange(row, col, 1, 2, b)))
            isVisited['2122'] = True
            dq.append((c+1, [2, 1], exchange(row, col, 2, 1, b)))
    return candidates
    for candidate in candidates:
        if isSame(candidate[1], board):
            return candidate[0]
    return -1


print(solution(board))
