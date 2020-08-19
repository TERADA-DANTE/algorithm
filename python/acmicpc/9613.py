from itertools import combinations
n = int(input())


def gcd(tuple):
    def execute(a, b):
        return b if not a % b else execute(b, a % b)
    [a, b] = [tuple[0], tuple[1]]
    return execute(a, b)


def solution(n):
    answer = [None] * n
    for i in range(n):
        numbers = combinations(map(int, input().split()[1:]), 2)
        answer[i] = sum(map(lambda t: gcd(sorted(t, reverse=1)), numbers))
    return '\n'.join(map(str, answer))


print(solution(n))
