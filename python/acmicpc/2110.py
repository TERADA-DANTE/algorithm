n, c = list(map(int, input().split()))


def solution(n, c):
    numbers = sorted([int(input()) for _ in range(n)])
    if c == 2:
        return numbers[-1] - numbers[0]
    1 2 4 8 9


print(solution(n, c))
