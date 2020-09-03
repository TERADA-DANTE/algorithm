from collections import deque
n, k = list(map(int, input().split()))


def solution(n, k):
    queue = deque(list(range(1, n+1)))
    answer = []
    i = 0
    while queue:
        t = (i+1) % k
        if not t:
            queue.rotate(-i)
            answer.append(queue.popleft())
            i = -1
        i += 1
    return '<' + ', '.join(list(map(str, answer))) + '>'


print(solution(n, k))
