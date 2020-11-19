from collections import deque
n = int(input())
k = int(input())
lines = [list(map(int, input().split())) for _ in range(k)]
answer = []


def solution(n, lines):
    board = [[] for _ in range(n)]
    for start, end, value in lines:
        board[end-1].append([start-1, value])
    dist = [0] * n

    def topology(array):
        queue = deque(array)
        order = []
        while queue:
            q = queue.popleft()
            order.append(q)

    topology([0])

#    return str(dp[0]) + '\n' + ' '.join(list(map(str, answer)))


print(solution(n, lines))
