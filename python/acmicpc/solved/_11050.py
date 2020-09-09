import sys
sys.setrecursionlimit(100000)
n, k = list(map(int, input().split()))


def solution(n, k):
    if k == 0 or n == k:
        return 1
    elif k == 1:
        return n
    else:
        return solution(n-1, k) + solution(n-1, k-1)


print(solution(n, k))
