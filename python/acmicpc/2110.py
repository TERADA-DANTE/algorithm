n, c = list(map(int, input().split()))


def solution(n, c):
    numbers = sorted([int(input()) for _ in range(n)])
    return numbers
    0 1 2 3 4      5   6    7
    0 2 5 8 1000 2000 5000 100000
    1 2 4 8 9
    0 - 1
    1 - 2


print(solution(n, c))
