n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def solution(n, board):
    return 1 << 0
    # 0 0 0에 있고, 0을 방문한상태
    # 1 2 3 4
    # 1 2 4 3
    # 1 3 2 4
    # 1 3 4 2
    # 1 4 2 3
    # 1 4 3 2


print(solution(n, board))
