import math
n, k = list(map(int, input().split()))

# DP!!


def solution(n, k):
    answers = [None, 1] + [None] * (k-1)
    for i in range(2, k+1):
        answers[i] = answers[i-1] * (n+1)
    return answers[-1] % 1000000000


print(solution(n, k))
