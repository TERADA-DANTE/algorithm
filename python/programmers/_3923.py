def solution(v):
    points = dict([[x, []] for x, _ in v])
    for x, y in v:
        points[x].append(y)
    l, r = sorted(list(points.keys()), key=lambda e: len(points[e]))
    return [l, *list(set(points[r]) - set(points[l]))]


print(solution([[1, 4], [1, 10], [3, 10]]))
