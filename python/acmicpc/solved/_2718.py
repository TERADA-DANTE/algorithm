answer = []


def solution(n):
    dp = [1, 1, 5, 11] + [None] * (n-3)
    for i in range(4, n+1):
        s = dp[i-1] + 4*dp[i-2]
        j = 3
        while i-j >= 0:
            s += [3, 2][j % 2] * dp[i-j]
            j += 1
        dp[i] = s
    return dp[n]


for _ in range(int(input())):
    n = int(input())
    answer.append(solution(n))
print('\n'.join(list(map(str, answer))))
