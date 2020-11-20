from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def solution(i, acc):
    global answer
    if i == n-1:
        if board[i][0] == 1:
            answer = max(answer, acc+board[i][1])
        else:
            answer = max(answer, acc)
        return
    elif i > n-1:
        answer = max(answer, acc)
        return
    else:
        index, value = board[i]
        if i+index <= n:
            solution(i+index, acc+value)
        solution(i+1, acc)


solution(0, 0)
print(answer)
