from collections import deque
n = int(input())
numbers = list(map(int, input().split()))
# LIS 이분탐색 복습


def solution(n, numbers):
    answer = 0
    queue = deque(numbers)
    stack = [queue.popleft()]
    while queue:
        q = queue.popleft()
        while stack and stack[-1] > q:
            stack.pop()
        stack.append(q)
        answer = max(answer, len(stack))
    return answer


print(solution(n, numbers))
