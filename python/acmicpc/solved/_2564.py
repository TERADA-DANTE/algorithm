col, row = list(map(int, input().split()))
n = int(input())

stores = [list(map(int, input().split())) for _ in range(n+1)]


def getCoordinates(position, distance):
    if position == 1:
        return [0, distance]
    elif position == 2:
        return [row, distance]
    elif position == 3:
        return [distance, 0]
    elif position == 4:
        return [distance, col]


def solution(row, col, n, stores):
    board = [[0] * (col+1) for _ in range(row+1)]
    R, C = getCoordinates(*stores.pop())
    coordinates = []
    answer = 0
    for pos, dist in stores:
        r, c = getCoordinates(pos, dist)
        coordinates.append([r, c])
        board[r][c] = 1
    for r, c in coordinates:
        if r == R:
            answer += abs(C-c)
        else:
            answer += abs(R-r)
            answer += min(C+c, col-c + col-C)
    return answer


print(solution(row, col, n, stores))
