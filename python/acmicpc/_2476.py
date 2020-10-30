n = int(input())
rolls = [list(map(int, input().split())) for _ in range(n)]


def solution(n, rolls):
    prices = [None] * n
    for i in range(n):
        a, b, c = rolls[i]
        if a == b == c:
            prices[i] = 10000+a*1000
        elif a == b != c:
            prices[i] = 1000+a*100
        elif a != b == c:
            prices[i] = 1000+b*100
        elif a == c != b:
            prices[i] = 1000+a*100
        else:
            prices[i] = sorted([a, b, c])[-1]*100
    return max(prices)


print(solution(n, rolls))
