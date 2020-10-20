from collections import deque
import sys
input = sys.stdin.readline
r, c = map(int, input().split())


def solution(r, c):
    board = [list(input().rstrip()) for _ in range(r)]
    # 각 노드의 최대 경로를 계산한다.
    # 각 노드는 방문했던 곳은 방문하지 않는다.
    answer = 1
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = set([(0, 0, board[0][0])])
    while queue:
        i, j, string = queue.pop()
        for a, b, in moves:
            row, col = i+a, j+b
            if 0 <= row < r and 0 <= col < c and (board[row][col] not in string):
                queue.add(
                    (row, col, string+board[row][col]))
                answer = max(answer, len(string)+1)
    return answer


print(solution(r, c))
