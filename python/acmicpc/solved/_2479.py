from collections import deque
from heapq import heappop, heappush
import bisect
import sys
input = sys.stdin.readline
n, k = list(map(int, input().split()))
numbers = [input().rstrip() for _ in range(n)]
start, end = list(map(int, input().split()))


def hamming(a, b):
    cnt = 2
    for i in range(k):
        if a[i] != b[i]:
            cnt -= 1
        if not cnt:
            return False
    return True


def solution(n, k, numbers):
    queue = deque([[0, start-1, f'{start}']])
    isVisited = [None] * n
    isVisited[start-1] = 0
    while queue:
        cnt, index, history = queue.popleft()
        if index == end-1:
            return history
        for i in range(n):
            if i == index:
                continue
            if isVisited[i]:
                continue
            isHamming = hamming(numbers[i], numbers[index])
            if not isHamming:
                continue
            isVisited[i] = True
            queue.append([cnt+1, i, history + f' {i+1}'])
    return -1


print(solution(n, k, numbers))
