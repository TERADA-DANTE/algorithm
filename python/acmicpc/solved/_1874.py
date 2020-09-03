from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
numbers = deque([int(input()) for _ in range(n)])


def solution(n, numbers):
    stack = []
    answer = []
    for i in range(1, n+1):
        stack.append(i)
        answer.append('+')
        for i in range(0, len(stack)):
            if numbers[0] != stack[-1]:
                break
            numbers.popleft()
            answer.append('-')
            stack.pop()
    return '\n'.join(answer) if not numbers else 'NO'


print(solution(n, numbers))
