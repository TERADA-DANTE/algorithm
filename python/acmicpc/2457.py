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
    left, right = d(1, 1), d(3, 1)
    flowers.sort(key=lambda v: (v[0], v[1], v[2], v[3]))
    queue = deque(flowers)
    while queue:
        print(answer)
        sM, sD, eM, eD = queue.popleft()
        start, end = d(sM, sD), d(eM, eD)
        if left == start:
            if answer and answer[-1][1] < end:
                answer.pop()
            left, right = start, end
            answer.append([start, end])
        elif left < start <= end:
            while len(answer) >= 2:
                if start <= answer[-2][1] and answer[-1][1] < end:
                    answer.pop()
                else:
                    break
            if right <= end:
                left, right = start, end
                answer.append([start, end])
        else:
            return 0
        if left <= d(3, 1) and d(11, 30) < right:
            return len(answer)
    return len(answer)


print(solution(n, flowers))
