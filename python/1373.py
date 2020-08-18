n = input()


def solution(n):
    return oct(int('0b'+n, 2))


print(solution(n)[2:])
