from collections import deque
n = int(input())

colors = deque(
    [list(map(lambda v: [v[0], int(v[1])], enumerate(input().split()))) for _ in range(n)])


def getBest(initial, color):
    idx, val = initial
    target = sorted([[i, v]
                     for i, v in color if i != idx], key=lambda v: v[1])
    return [target[0][0], val+target[0][1]]


def solution(colors):
    while len(colors) > 1:
        print(colors)
        color = colors.pop()
        initials = colors.pop()
        colors.append([getBest(initial, color) for initial in initials])
    return min(list(map(lambda v: v[1], colors[0])))


print(solution(colors))
