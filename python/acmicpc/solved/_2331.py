# from collections import deque
a, p = list(map(int, input().split()))


def solution(a, p):
    d = [a]
    while True:
        n = sum(map(lambda v: int(v)**p, list(str(d[-1]))))
        if n not in d:
            d.append(n)
        else:
            print(d, n)
            return d.index(n)


print(solution(a, p))
