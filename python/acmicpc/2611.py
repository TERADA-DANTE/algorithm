from collections import deque
from heapq import heappush, heappop
n = int(input())
k = int(input())
lines = [list(map(int, input().split())) for _ in range(k)]


def solution(n, lines):
    board = [[0] * n for _ in range(n)]
    for start, end, value in lines:
        board[start-1][end-1] = value
    queue = deque([[0, 0, [0]]])
    # heap
    result = []
    while queue:
        vertex, value, history = queue.popleft()
        for i in range(n):
            if board[vertex][0]:
                heappush(result, (-(value+board[vertex][0]), history+[0]))
            if i not in history and board[vertex][i]:
                queue.append([i, value+board[vertex][i], history+[i]])
    count, answer = heappop(result)
    return str(-count) + '\n' + ' '.join(list(map(lambda v: str(v+1), answer)))


print(solution(n, lines))
