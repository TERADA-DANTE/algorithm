from collections import deque
m, n = list(map(int, input().split()))
comparisons = [list(map(int, input().split())) for _ in range(n)]


def getZeros(entries):
    return [i for i in range(m) if not entries[i]]


def solution(m, n, comparisons):
    graph = [[] for _ in range(m)]
    entries = [0] * m
    result = []
    for a, b in comparisons:
        graph[a-1].append(b-1)
        entries[b-1] += 1

    queue = deque(getZeros(entries))
    while queue:
        q = queue.popleft()
        result.append(q+1)
        for i in graph[q]:
            entries[i] -= 1
            if not entries[i]:
                queue.append(i)
    return ' '.join(list(map(str, result)))


print(solution(m, n, comparisons))
