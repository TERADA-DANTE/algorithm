a = int(input())
A = list(input())
b = int(input())
B = list(input())


def solution(a, b, A, B):
    dp = [[0]*(a+1) for _ in range(b+1)]
    for i in range(b+1):
        for j in range(a+1):
            if not i:
                if j:
                    dp[i][j] = -2*j
            elif not j:
                if i:
                    dp[i][j] = -2*i
            else:
                candidates = [dp[i-1][j], dp[i][j-1], dp[i-1][j-1]]
                if B[i-1] == A[j-1]:
                    print(i, j)
                    dp[i][j] = max(dp[i-1][j-1]+3, 3)
                else:
                    dp[i][j] = max(candidates)-2
    for i in range(b+1):
        print(*dp[i])
    answer = 0
    for i in range(b+1):
        for j in range(a+1):
            if answer < dp[i][j]:
                answer = dp[i][j]
                row, col = i, j
    return answer, row, col


print(solution(a, b, A, B))
