n = int(input())
k = int(input())
pairs = [list(map(int, input().split())) for _ in range(k)]


class Union:
    def __init__(self, data):
        self.node = [i for i in range(data+1)]

    def _find(self, i):
        if self.node[i] != i:
            return self._find(self.node[i])
        return i

    def set(self, x, y):
        parent, child = sorted([self._find(x), self._find(y)])
        self.node[child] = parent


def solution(n, pairs):
    union = Union(n)
    cnt = 0
    for x, y in pairs:
        union.set(x, y)
    for i in range(n+1):
        if union._find(i) == 1:
            cnt += 1
    return cnt-1


print(solution(n, pairs))
