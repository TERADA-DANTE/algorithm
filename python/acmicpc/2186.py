n, m, k = list(map(int, input().split()))
board = [list(input()) for _ in range(n)]
target = input() + ' '
answer = []
cnt = 0
dp = [[[None]*len(target) for _ in range(m)] for _ in range(n)]

# DFS + DP


def getInitial(board, t):
    result = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == t:
                result.append([i, j])
    return result


def getNext(pre, i, h):
    global cnt
    r, c = pre
    next = []
    for t in range(1, k+1):
        # 위
        for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            if dp[r+x*t][c+y*t][i] == 0:
                continue
            elif dp[r+x*t][c+y*t][i]:

        if r-x >= 0 and board[r-x][c] == target[i]:
            next.append([r-x, c])
            # 아래
        if r+x < n and board[r+x][c] == target[i]:
            next.append([r+x, c])
            # 오른쪽
        if c+x < m and board[r][c+x] == target[i]:
            next.append([r, c+x])
            # 왼쪽
        if c-x >= 0 and board[r][c-x] == target[i]:
            next.append([r, c-x])
    if next:
        for cur in next:
            getNext(cur, i+1, h+[cur])
    elif not next and len(h) != len(target) - 1:
        row, col = h[-1]
        dp[row][col][len(h)-1] = 0
    else:
        for i, v in enumerate(h):
            row, col = v
            dp[row][col][i] = dp[row][col][i] + 1 if dp[row][col][i] else 1


def solution(board):
    for pre in getInitial(board, target[0]):
        getNext(pre, 1, [pre])
    return cnt


print(solution(board))
