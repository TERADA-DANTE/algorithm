from collections import deque
n = int(input())
history = []
board = [None] * n
isVisited = [None] * n
steps = [[0, 1], [1, 0], [-1, 0], [0, -1]]


# BFS 로 찾아주세용~
def move(i, j, cnt=1):
    dq = deque([[i, j]])
    history = []
    while dq:
        q = dq.popleft()
        isVisited[q[0]][q[1]] = True
        if q not in history:
            history.append(q)
            next = [[q[0]+step[0], q[1]+step[1]] for step in steps if 0 <=
                    q[0]+step[0] < n and 0 <= q[1]+step[1] < n and board[q[0]+step[0]][q[1]+step[1]] and not isVisited[q[0]+step[0]][q[1]+step[1]]]
            dq += next
    return len(history)


def solution(n):
    answer = []
    for i in range(n):
        board[i] = list(map(int, list(input())))
        isVisited[i] = [None] * n
    for i in range(n):
        for j in range(n):
            if not isVisited[i][j] and board[i][j]:
                answer.append(move(i, j))
    return '\n'.join(map(str, [len(answer)]+list(map(str, sorted(answer)))))


print(solution(n))
