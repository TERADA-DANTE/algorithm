n = input()


def solution(n):
    return bin(int('0o'+n, 8))


print(solution(n)[2:])
