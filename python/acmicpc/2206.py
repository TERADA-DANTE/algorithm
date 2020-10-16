import sys
row, col = list(map(int, input().split()))
sys.setrecursionlimit(10000000)
answer = float('inf')


def solution(row, col):
    board = [list(map(int, list(input()))) for _ in range(row)]
    isVisited = [[0] * col for _ in range(row)]
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def execute(r=0, c=0, isPassed=0, cnt=0):
        global answer
        if r == row-1 and c == col-1:
            answer = min(answer, cnt)
            return
        for a, b in moves:
            x, y = r+a, c+b
            if 0 <= x < row and 0 <= y < col:
                if not isVisited[x][y] and (isPassed+board[x][y]) < 2:
                    isVisited[x][y] = True
                    execute(x, y, isPassed+board[x][y], cnt + 1)
                    isVisited[x][y] = False

    execute()
    return -1 if answer == float('inf') else answer+1
# DFS를 사용하여 가능한 경우 계속해서 해 나간다.
# 탐색이 끝나면 되돌린다.


print(solution(row, col))
