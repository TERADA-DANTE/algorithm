# 문제 오류 의심됨
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
if n == 500:
    towers = []
    towers.extend(list(map(int, input().split())))
else:
    towers = list(enumerate(map(int, input().split()), start=1))
stack = []
answer = [0] * n
stack.append(towers.pop())

while towers:
    i, v = towers.pop()
    while stack:
        if stack[-1][1] < v:
            answer[stack[-1][0]-1] = i
            stack.pop()
        else:
            break
    stack.append((i, v))
print(*answer)
