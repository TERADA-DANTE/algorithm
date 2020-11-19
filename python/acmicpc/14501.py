from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# 경계조건 너무 귀찮아


def solution(i, acc):
    global answer
    if i >= n:
        return
    index, value = board[i]
    if i + index <= n:
        answer = max(answer, acc+value)
        solution(i+index, acc+value)
        solution(i+1, acc)
    else:
        return


solution(0, 0)
print(answer)
