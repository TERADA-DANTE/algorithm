n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]


def solution(n, triangle):
    dp = [triangle[0]]
    for i in range(n-1):
        dp.append([0]*(i+2))
        for j in range(i+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i]
                               [j] + triangle[i+1][j+1])
    return max(dp[-1])


print(solution(n, triangle))
