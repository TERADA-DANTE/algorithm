from collections import deque
import sys
input = sys.stdin.readline
n, k = list(map(int, input().split()))
numbers = [int(input().rstrip(), 2) for _ in range(n)]
s, e = list(map(int, input().split()))
start, end = numbers[s-1], numbers[e-1]


def solution(n, k, numbers):
    isVisited = [None] * n
    adjacents = [[] for _ in range(n)]


print(*solution(n, k, numbers))
