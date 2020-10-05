from collections import deque
k, n = list(map(int, input().split()))
lines = deque([list(map(int, input().split())) for _ in range(n)])
start = int(input())
ladders = [None] * k
while lines:
    a, b = lines.popleft()
    if a == start:
        start = b
    elif b == start:
        start = a
print(start)
