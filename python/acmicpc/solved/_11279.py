from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline
n = int(input())


def solution(n):
    heap = []
    answer = []
    for _ in range(n):
        x = int(input())
        if x:
            heappush(heap, -x)
        else:
            if heap:
                answer.append(-heappop(heap))
            else:
                answer.append(0)
    return '\n'.join(list(map(str, answer)))


print(solution(n))
