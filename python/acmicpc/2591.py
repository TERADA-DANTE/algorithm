
n = input()


def solution(n):
    dp = [0] * (len(n)+1)

    def DFS(string, i):
        if dp[i]:
            return dp[i]
        if not string:
            dp[i] = 1
            return 1
        if not int(string[0]):
            return 0
        if len(string) > 1:
            if 1 <= int(string[0]) <= 34 and 1 <= int(string[:2]) <= 34:
                dp[i] = DFS(string[1:], i+1) + DFS(string[2:], i+2)
                return dp[i]
            if 1 <= int(string[0]) <= 34:
                dp[i] = DFS(string[1:], i+1)
                return dp[i]
        else:
            if 1 <= int(string[0]) <= 34:
                dp[i] = DFS(string[1:], i+1)
                return dp[i]
    DFS(n, 0)
    return dp[0]


print(solution(n))
