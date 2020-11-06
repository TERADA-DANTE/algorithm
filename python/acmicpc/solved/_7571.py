import sys

input = sys.stdin.readline
n, m = list(map(int, input().split()))
points = [list(map(int, input().split())) for _ in range(m)]


def dist(x, y):
    ret = 0
    for a, b in points:
        ret += abs(a-x)+abs(b-y)
    return ret


def middle(arr):
    l = len(arr)
    if l % 2:
        return [arr[int(l//2)]]
    else:
        return [arr[int(l//2)-1], arr[int(l//2)]]


def solution(n, m, points):
    xs = middle(sorted([x for x, y in points]))
    ys = middle(sorted([y for y, y in points]))
    if len(xs) == 1:
        candidate = [xs[0], ys[0]]
        return dist(*candidate)
    else:
        candidates = [[xs[0], ys[0]], [xs[0], ys[1]],
                      [xs[1], ys[0]], [xs[1], ys[1]]]
        return min([dist(*candidate) for candidate in candidates])


print(solution(n, m, points))
