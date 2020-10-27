from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def solution(n, board):
    global answer
    bishops = [[i, j] for j in range(n) for i in range(n) if board[i][j]]
    queue = deque([[bishops, 0]])
    while queue:
        bishop, cnt = queue.popleft()
        if bishop:
            i, j = bishop.pop()
            queue.append([bishop, cnt])
            newBishop = []
            for r, c in bishop:
                newBishop.append([r, c])
                for k in range(n):
                    if i+k == r and j+k == c:
                        newBishop.pop()
                        break
                    if i+k == r and j-k == c:
                        newBishop.pop()
                        break
                    if i-k == r and j+k == c:
                        newBishop.pop()
                        break
                    if i-k == r and j-k == c:
                        newBishop.pop()
                        break

            queue.append([newBishop, cnt+1])
        else:
            answer = max(answer, cnt)
    return answer


print(solution(n, board))
