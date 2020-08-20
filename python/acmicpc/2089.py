n = int(input())


def solution(n):
    if n >= 0:
        return bin(n)[2:]


print(solution(n))
