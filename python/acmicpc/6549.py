from collections import deque
answer = []


def solution(n, h):
    dp = [None] * n
    heights = deque(enumerate(h))
    stack = deque([heights.popleft()])
    while heights:
        idx, val = heights.popleft()
        if val < stack[-1][1]:
            while stack:

                length = len(stack)
                index, value = stack.popleft()
                dp[index] = value * length
        stack.append((idx, val))
    print(dp, stack)
    return dp


while True:
    n, *h = list(map(int, input().split()))
    if not n:
        break
    answer.append(solution(n, h))
print('\n'.join(list(map(str, answer))))
