import time
n = int(input())
k = int(input())


def f(n, m):
    return [n*i for i in range(1, m+1)]


def solution(n, k):
    return [f(i, n) for i in range(1, n+1)]
    #    1    2     3     4     5       6
    #    2    4     6     8     10      12
    #    3    6     9     12    15      18
    #    4    8     12    16    20      24
    #    5    10    15    20    25      30
    #    6    12    18    24    30      36

    # # 행과 열이 작다면 작다.
    # 123 246 369
    # 1 2 2 3 3 4 6 6 9
    # row = int(k//n)
    # col = k % n
    # return (row)


print(solution(n, k))
