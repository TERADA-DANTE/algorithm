from collections import deque


def solution(n, cnt=0):
    def DFS(i):
        isVisit[i] = True
        if not isVisit[numbers[i]]:
            DFS(numbers[i])
        return
    numbers = [None] + list(map(int, input().split()))
    isVisit = [False] * (n+1)
    for i in range(1, n+1):
        if not isVisit[i]:
            DFS(i)
            cnt += 1
    return cnt


for _ in range(int(input())):
    print(solution(int(input())))
