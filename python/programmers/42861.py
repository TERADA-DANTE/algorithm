from collections import deque


def union(i, j, parents):
    if i < j:
        parents[j] = i
    else:
        parents[i] = j
    return parents


def getParent(i, parents):
    if parents[i] == i:
        return i
    return getParent(parents[i], parents)


def solution(n, costs):
    parents = [i for i in range(n)]
    dq = deque(sorted(costs, key=lambda v: (v[2], v[0], v[1])))
    s = 0
    while n-1:
        v, w, i = dq.popleft()
        a = getParent(v, parents)
        b = getParent(w, parents)
        if a != b:
            parents = union(v, w, parents)
            s += i
            n -= 1
    return s


print(solution(4, [[0, 1, 1], [0, 2, 2], [2, 3, 1]]))
print(solution(4, [[0, 1, 1], [0, 2, 2], [
      0, 3, 1], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
print(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [
      1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]))
print(solution(1, []))
