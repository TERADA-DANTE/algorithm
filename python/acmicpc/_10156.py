k, n, m = list(map(int, input().split()))


def solution(k, n, m):
    return k*n-m if k*n-m > 0 else 0


print(solution(k, n, m))
