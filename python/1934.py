n = int(input())


def gcd(a, b):
    return b if not a % b else gcd(b, a % b)


def solution(n):
    answer = []
    for _ in range(n):
        b, a = sorted(map(int, input().split()))
        answer.append(int(a*b/gcd(a, b)))
    return '\n'.join(map(str, answer))


print(solution(n))
