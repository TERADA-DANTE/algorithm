from heapq import heappop, heappush
from collections import deque
import sys
input = sys.stdin.readline
n, k = list(map(int, input().split()))
numbers = [input().rstrip() for _ in range(n)]
s, e = list(map(int, input().split()))


def hamming(current, number):
    a = int('1'+current, 2)
    b = int('1' + number, 2)
    return bin(a ^ b).count('1') == 1


def solution(n, k, numbers):
    board = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if hamming(numbers[i], numbers[j]):
                board[i].append(j+1)
                board[j].append(i+1)
    heap = [(0, [s], numbers[s-1])]
    while heap:
        cnt, history, number = heappop(heap)
        h = history[-1]
        if number == numbers[e-1]:
            return history
        for v in board[h-1]:
            if v not in history:
                heappush(heap, (cnt+1, history+[v], numbers[v-1]))
    return [-1]


print(*solution(n, k, numbers))
