import sys
from collections import deque
input = sys.stdin.readline
t = int(input())


def DFS(arr, i, cnt):
    global isDone
    [dq, history] = [deque([i]), []]
    while dq:
        q = dq.pop()
        if q not in history:
            history.append(q)
            dq.append(arr[q])
    e = history[-1]
    print('hi', history)
    if history[0] == arr[e]:
        print('hi', history)
        for h in history:
            isDone[h] = True
        return len(history)
    else:
        for h in history[:-1]:
            isDone[h] = True
        return 0


def solution(n, cnt=0):
    for i in range(1, n+1):
        if not isDone[i]:
            cnt += DFS(students, i, cnt)
            print(isDone)
    return n - cnt


for _ in range(t):
    n = int(input())
    isDone = [None] + [None] * n
    students = [None] + list(map(int, input().split()))
    print(solution(n))
