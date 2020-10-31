from itertools import combinations
from collections import deque
n, k = list(map(int, input().split()))
numbers = [input() for _ in range(n)]
s, e = list(map(int, input().split()))

arr = list(combinations([i for i in range(n)], 2))

board = [[0] * n for _ in range(n)]


def hamming(path, number, k):
    # 비트 마스킹
    p = '0b1'+path
    t = '0b1'+number
    cnt = 0
    for i in range(k):
        if path[i] != number[i]:
            cnt += 1
    return cnt


for a, b in arr:
    board[a][b] = board[b][a] = hamming(numbers[a], numbers[b], k)


def solution(n, k, numbers):
    start, end = numbers[s-1], numbers[e-1]
    queue = deque([[start, [s-1]]])
    while queue:
        path, history = queue.popleft()
        a = history[-1]
        if path == end:
            return list(map(lambda v: v+1, history))
        for i in range(n):
            if board[a][i] == 1 and i not in history:
                queue.append([numbers[i], history+[i]])
    return [-1]


print(*solution(n, k, numbers))
