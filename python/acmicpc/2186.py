import time
n, m, k = list(map(int, input().split()))
board = [list(input()) for _ in range(n)]
target = input() + ' '
answer = []
cnt = 0
memo = dict()
for i in range(n):
    for j in range(m):
        if board[i][j] in list(target):
            memo[f'{i}{j}'] = board[i][j]


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
    for x in range(1, k+1):
        # 위
        if memo.get(f'{r-x}{c}'):
            if memo[f'{r-x}{c}'] == target[i]:
                getNext([r-x, c], i+1, h+1)
            # 아래
        if memo.get(f'{r+x}{c}'):
            if memo[f'{r+x}{c}'] == target[i]:
                getNext([r+x, c], i+1, h+1)
            # 오른쪽
        if memo.get(f'{r}{c+x}'):
            if memo[f'{r}{c+x}'] == target[i]:
                getNext([r, c+x], i+1, h+1)
            # 왼쪽
        if memo.get(f'{r}{c-x}'):
            if memo[f'{r}{c-x}'] == target[i]:
                getNext([r, c-x], i+1, h+1)
    if h == len(target)-1:
        cnt += 1


def solution(board):
    print(memo)
    for pre in getInitial(board, target[0]):
        getNext(pre, 1, 1)
    return cnt


s = time.time()
print(solution(board))
print(time.time() - s)
