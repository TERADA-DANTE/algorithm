n = int(input())
numbers = sorted(list(map(int, input().split())), key=lambda v: -v)


def solution(n, numbers):
    return numbers[0] * numbers[-1]


print(solution(n, numbers))
