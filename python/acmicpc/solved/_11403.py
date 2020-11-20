from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def solution(n, board):
    def BFS(i):
        queue = deque([i])
        isVisited = [None] * n
        #isVisited[i] = True
        while queue:
            q = queue.pop()
            for j in range(n):
                if board[q][j] and not isVisited[j]:
                    isVisited[j] = True
                    queue.append(j)
        return [1 if isVisited[i] else 0 for i in range(n)]
    return '\n'.join([' '.join(list(map(str, BFS(i)))) for i in range(n)])


print(solution(n, board))
