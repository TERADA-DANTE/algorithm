from collections import deque
n = int(input())
numbers = list(map(int, input().split()))
difs = [numbers[i]-numbers[i-1] for i in range(1, n)]
for i in range(n-1):
    if difs[i] != 1:
        start = i+1
        if difs[i+1] == 1:
            end = i-1
print(start, end)
