a, b = list(map(int, input().split()))


def gcd(a, b):
    return b if not a % b else gcd(b, a % b)


def solution(a, b):
    b, a = sorted([a, b])
    return '1'*gcd(a, b)


print(solution(a, b))
