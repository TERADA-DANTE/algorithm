n, m, t, k = list(map(int, input().split()))
coordinates = [list(map(int, input().split())) for _ in range(t)]


def solution(n, m, t, k, coordinates):
    def countGem(i, j, k):
        temp = 0
        for l in range(k+1):
            temp += board[i+l][j:j+k+1].count(1)
        return temp
    board = [[0] * (n+1) for _ in range(m+1)]
    answer = 0
    for C, r in coordinates:
        R = m-r
        board[R][C] = 1
    for i in range(m-k+1):
        for j in range(n-k+1):
            gem = countGem(i, j, k)
            if answer <= gem:
                answer = gem
                x, y = j, m-i

    return f'{x} {y}\n{answer}'


print(solution(n, m, t, k, coordinates))
