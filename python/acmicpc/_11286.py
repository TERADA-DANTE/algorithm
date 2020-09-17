from heapq import *
n = int(input())
heap = []
answer = []
for _ in range(n):
    x = int(input())
    if x:
        heappush(heap, (abs(x), x))
    else:
        if heap:
            answer.append(heappop(heap)[1])
        else:
            answer.append(0)
print('\n'.join(list(map(str, answer))))
