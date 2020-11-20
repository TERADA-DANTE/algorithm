from itertools import combinations
n, s = list(map(int, input().split()))
numbers = sorted(map(int, input().split()))
cnt = 0


def solution():
    global cnt
    for i in range(1, n+1):
        candidates = list(combinations(numbers, i))
        for candidate in candidates:
            sumC = sum(candidate)
            if sumC == s:
                cnt += 1

    return cnt


print(solution())
