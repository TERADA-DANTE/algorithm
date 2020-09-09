n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]


def solution(n, lines):
    dp = [0]
    lines.sort(key=lambda v: v[0])
    for i in range(1, n):
        line = lines[i][1]
        candidates = []
        for j in range(0, i):
            if lines[j][1] < line:
                candidates.append(j)
        if candidates:
            dp.append(max(list(map(lambda v: dp[v], candidates))) + 1)
        else:
            dp.append(0)
    return n - max(dp) - 1


print(solution(n, lines))
# 가장 긴 증가하는 부분수열 구하기 문제
