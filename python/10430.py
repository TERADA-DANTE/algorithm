a, b = list(map(int, input().split()))


def gcd(a, b):
    return b if not a % b else gcd(b, a % b)


def solution(a, b):
    [b, a] = sorted([a, b])
    g = gcd(a, b)
    return '\n'.join(map(str, [g, int(a*b/g)]))


print(solution(a, b))
