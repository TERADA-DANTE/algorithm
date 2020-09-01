from collections import deque
n = int(input())
l, r = list(map(int, input().split()))
targets = []
for _ in range(int(input())):
    targets.append(int(input()))


def solution(n, l, r, targets):
    # val, [l, r]
    queue = deque([[0, [l, r]]])
    while targets:
        l = len(queue)
        target = targets.popleft()
        for _ in range(l):
            val, [l, r] = queue.popleft()
            if l <= target <= r:
                queue.append([val+target-l, [target, r]])
                queue.append([val+r - target, [l, target]])
            elif target < l:
                queue.append([val+l - target, [target, r]])
            elif r < target:
                queue.append([val+target-r, [l, target]])
    m = float('inf')
    while queue:
        q = queue.popleft()
        if m > q[0]:
            m = q[0]
    return m


print(solution(n, l, r, deque(targets)))
