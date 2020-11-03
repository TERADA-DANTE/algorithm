from collections import deque
n = int(input())
flowers = [list(map(int, input().split())) for _ in range(n)]
# 4, 6, 9, 11월은 30일까지 있고,
# 1, 3, 5, 7, 8, 10, 12월은 31일까지 있으며,
# 2월은 28일까지만 있다.
# 1월 1일 ~ 12월 31일
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = [None] * (1+31*7+28+30*4)
# n월 n일은 n-1월까지 월 수 다 더하고,
# n월 n일 == months[0:n]+m
answer = []


def d(month, day): return sum(months[0:month])+day


def solution(n, flowers):
    global answer

    flowers.sort(key=lambda v: (v[0], v[1], v[2], v[3]))
    queue = deque(flowers)
    if d(3, 1) < d(queue[0][0], queue[0][1]):
        return 0
    while queue:

        sM, sD, eM, eD = queue.popleft()
        start, end = d(sM, sD), d(eM, eD)
        if start == end:
            continue
        if not answer:
            answer.append([start, end])
            continue
        tip = answer[-1][1]
        if tip < start:
            return 0
        if end <= tip:
            continue
        while answer:
            r = answer[-2][1] if len(answer) > 1 else d(3, 1)
            if start <= r:
                answer.pop()
            else:
                break
        answer.append([start, end])
        min = answer[0][0]
        max = answer[-1][-1]
        if min <= d(3, 1) and d(11, 30) < max:
            return len(answer)
    return 0


print(solution(n, flowers))
