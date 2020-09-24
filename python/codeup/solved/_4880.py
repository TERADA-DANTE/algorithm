from collections import deque
n, k = list(map(int, input().split()))

costs = deque(list(map(int, input().split())) for _ in range(n))

queue = deque([[0, 0]])
while costs:
    t1, c1, t2, c2 = costs.popleft()
    for _ in range(len(queue)):
        t, c = queue.popleft()
        if t+t1 <= k:
            queue.append([t+t1, c+c1])
        if t+t2 <= k:
            queue.append([t+t2, c+c2])
print(sorted(queue, key=lambda v: -v[1])[0][1])
