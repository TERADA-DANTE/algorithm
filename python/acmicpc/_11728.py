import sys
from collections import deque
input = sys.stdin.readline
n, m = list(map(int, input().split()))
a = deque(map(int, input().split()))
b = deque(map(int, input().split()))


def solution(a, b):
    answer = []
    while a and b:
        if a[0] > b[0]:
            answer.append(b.popleft())
        else:
            answer.append(a.popleft())
    return answer + list(a+b)


print(' '.join(map(str, solution(a, b))))
