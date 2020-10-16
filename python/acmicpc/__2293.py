n, k = list(map(int, input().split()))


def solution(n, k):
    coins = [int(input()) for _ in range(n)]
    cases = [1] + [0] * (k)
    for coin in coins:
        for i in range(k+1):
            if i >= coin:
                cases[i] = cases[i] + cases[i-coin]

    return cases[-1]


print(solution(n, k))
