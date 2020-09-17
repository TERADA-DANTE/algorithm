import sys
from heapq import *
input = sys.stdin.readline
n = int(input())


def solution(n):
    heap = []
    answer = []
    for _ in range(n):
        heappush(heap, int(input()))
        l = len(heap)
        if l % 2:
            temp = []
            for _ in range(l//2):
                heappush(temp, heappop(heap))
            x = heappop(heap)
            answer.append(x)
            heappush(temp, x)
            heap = list(merge(temp, heap))
            heapify(heap)
        else:
            temp = []
            for _ in range(l//2 - 1):
                heappush(temp, heappop(heap))
            x = heappop(heap)
            y = heappop(heap)
            answer.append(min(x, y))
            heappush(temp, x)
            heappush(temp, y)
            heap = list(merge(temp, heap))
            heapify(heap)
    return '\n'.join(list(map(str, answer)))


print(solution(n))
