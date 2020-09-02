from collections import deque
import re
import sys
input = sys.stdin.readline
answer = []


def solution(p, numbers):
    p = list(re.sub(r'RR', '', p))
    i = 0
    for j in range(len(p)):
        if p[j] == 'R':
            i += 1
        elif i % 2:
            p[j] = 'L'
    k = 0
    for s in p:
        if s == 'R':
            k += 1
        elif s == 'L':
            if len(numbers):
                numbers.pop()
            else:
                return 'error'
        else:
            if len(numbers):
                numbers.popleft()
            else:
                return 'error'
    return re.sub(r' ', '', str(list(numbers) if not k % 2 else list(reversed(numbers))))


for _ in range(int(input())):
    p = input()[:-1]
    n = int(input())
    numbers = list(map(int, re.findall(r'\d+', input())))
    answer.append(solution(p, deque(numbers)))
print('\n'.join(answer))
