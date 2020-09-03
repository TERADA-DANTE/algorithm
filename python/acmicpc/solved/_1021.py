from collections import deque
n, m = list(map(int, input().split()))

index = deque(list(map(lambda v: int(v), input().split())))


def solution(n, m, index):
    cnt = 0
    queue = deque(list(range(1, n+1)))
    while index:
        i = index.popleft()
        l = queue.index(i)
        queue.reverse()
        r = queue.index(i)+1
        queue.reverse()
        if l < r:
            queue.rotate(-l)
            queue.popleft()
            cnt += l
        else:
            queue.rotate(r)
            queue.popleft()
            cnt += r
    return cnt


print(solution(n, m, index))
