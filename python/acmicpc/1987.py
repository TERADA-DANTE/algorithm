from collections import deque
r, c = list(map(int, input().split()))
max = 0


def solution(r, c):
    global max
    board = [list(input()) for _ in range(r)]
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]


print(solution(r, c))
