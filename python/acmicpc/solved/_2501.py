n, k = list(map(int, input().split()))


def solution(n, k):
    divisors = [i for i in range(1, n+1) if not n % i]
    return divisors[k-1] if k <= len(divisors) else 0


print(solution(n, k))
