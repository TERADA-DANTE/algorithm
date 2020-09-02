from collections import deque
answer = []


def solution(queue, m):
    result = []
    while queue:
        q = queue.popleft()
        result.append(q)
        for que in queue:
            if que[1] > q[1]:
                queue.append(q)
                result.pop()
                break
    for i in range(len(result)):
        if result[i][0] == m:
            return i+1


for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    queue = deque(
        list(zip(list(range(n)), list(map(int, input().split())))))
    answer.append(solution(queue, m))
print('\n'.join(list(map(str, answer))))
