n = int(input())
coordinates = [list(map(int, input().split())) for _ in range(n)]


def solution(n, coordinates):
    board = [[0] * 100 for _ in range(100)]
    answer = 0
    for col, r in coordinates:
        row = 100-r-1
        for i in range(10):
            for j in range(10):
                board[row+i-10][col+j] = 1
    for i in range(100):
        for j in range(100):
            answer += board[i][j]
    return answer


print(solution(n, coordinates))
