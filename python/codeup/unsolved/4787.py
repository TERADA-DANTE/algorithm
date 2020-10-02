from collections import deque
n, c = list(map(int, input().split()))
k = int(input())
boxes = [list(map(int, input().split())) for _ in range(k)]
boxes.sort(key=lambda v: (v[0], v[1]))
queue = deque(boxes)
acc = 0
truck = [0] * (n+1)
# 1번 마을에 간다.
# 2번 마을꺼 다싣는다.
# 3번 마을꺼 다 싣는다.
...
# n 번 마을꺼까지 용량이 되는 대로 다 싣는다.

# 2번 마을에 간다.
# 내린다.
# 3번 마을꺼 다 싣는다.
# n 번 마을꺼까지 용량이 되는 대로 다 싣는다.
capacity = c
for i in range(1, n+1):
    acc += truck[i]
    capacity += truck[i]
    truck[i] = 0
    while True:
        if queue and queue[0][0] == i:
            f, t, l = queue.popleft()
            if capacity:
                truck[t] += min(capacity, l)
                capacity = capacity - l if capacity >= l else 0
        else:
            break
print(acc)
