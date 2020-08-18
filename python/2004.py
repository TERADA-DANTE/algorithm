n, m = list(map(int, input().split()))


def solution(n, m):
    memo = {}

    def combinations(a, b):
        if memo.get(f"{a}C{b}"):
            return memo[f"{a}C{b}"]
        elif b == 1:
            return a
        memo[f"{a}C{b}"] = combinations(a-1, b) + combinations(a-1, b-1)


pritn(solution(n, m))
