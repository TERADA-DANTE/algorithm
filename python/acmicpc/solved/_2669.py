coordinates = [list(map(int, input().split())) for _ in range(4)]


def solution(coordinates):
    board = [[0] * 100 for _ in range(100)]
    answer = 0
    for x1, y1, x2, y2 in coordinates:
        row = 100-y2
        col = x1
        for i in range(y2-y1):
            for j in range(x2-x1):
                board[row+i][col+j] = 1
    for i in range(100):
        for j in range(100):
            answer += board[i][j]
    return answer


print(solution(coordinates))
