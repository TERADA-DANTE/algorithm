row, col = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(row)]
answer = 1


def isValid(r, c):
    return 0 <= r < row and 0 <= c < col

# 0 : up
# 1 : right
# 2 : down
# 3 : left
# 클래스로 풀고싶다.


def solution():
    global answer, r, c, d
    isVisited = [[None] * col for _ in range(row)]
    isVisited[r][c] = True
    while True:
        if isValid(r, c-1) and not board[r][c-1] and not isVisited[r][c-1]:
            c -= 1
            answer += 1


print(solution())
