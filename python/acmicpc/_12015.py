from collections import deque
n = int(input())
numbers = list(map(int, input().split()))


def solution(n, numbers):
    queue = deque(numbers)
    stack = [queue.popleft()]
    while queue:
        q = queue.popleft()
        l, r = 0, len(stack)
        while l < r:
            mid = int((l+r)/2)
            if q <= stack[mid]:
                r = mid
            else:
                l = mid+1
        if r+1 > len(stack):
            stack.append(q)
        else:
            stack[r] = q
    return len(stack)


print(solution(n, numbers))
