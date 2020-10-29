from itertools import combinations
from collections import deque
n = int(input())

temp = [list(map(int, input().split())) for _ in range(n)]
lines = [sorted(line) for line in temp]


def isCross(a, b, arr):
    for x, y in arr:
        if sum([1 if x <= a <= y else 0, 1 if x <= b <= y else 0]) == 1:
            return True
    return False


def solution(n, lines):
    queue = deque(list(enumerate([[line] for line in lines])))
    answer = 0
    while queue:

        index, arr = queue.popleft()
        answer = max(answer, len(arr))
        for i in range(index+1, n):
            if not isCross(*lines[i], arr):
                queue.append([i, arr+[lines[i]]])
    return answer


print(solution(n, lines))
