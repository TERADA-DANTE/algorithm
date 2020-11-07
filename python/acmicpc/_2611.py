from collections import deque
from heapq import heappush, heappop
n = int(input())
k = int(input())
lines = [list(map(int, input().split())) for _ in range(k)]


def solution(n, lines):
    board = [[0] * n for _ in range(n)]
    for start, end, value in lines:
        board[start-1][end-1] = value
    dist = [0] * n
    history = [i for i in range(n)]
    isVisited = [None] * n
    queue = deque([[0, 0]])
    while queue:
        index, value = queue.popleft()
        isVisited[index] = True
        if not index and value:
            continue
        for i in range(n):
            v = board[index][i]
            if v and dist[i] < v+value:
                dist[i] = v+value
                history[i] = index
                queue.append([i, value+v])
    answer = [0]
    while history[answer[-1]]:
        answer.append(history[answer[-1]])
    answer += [0]

    return str(dist[0]) + '\n' + ' '.join(list(map(lambda v: str(v+1), list(reversed(answer)))))


print(solution(n, lines))
