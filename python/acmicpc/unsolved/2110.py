n, c = list(map(int, input().split()))


def solution(n, c):
    numbers = sorted([int(input()) for _ in range(n)])
    if c == 2:
        return numbers[-1] - numbers[0]
# 모르겠어..


print(solution(n, c))
