n = int(input())
numbers = list(map(int, input().split()))


def solution(n, numbers):
    dp = [0] * 1000001
    for i in range(1, n):
        if numbers[i] < numbers[i-1]:
            break
    else:
        return 0
    for i in range(n):
        dp[numbers[i]] = dp[numbers[i]-1]+1
    return n - max(dp)


print(solution(n, numbers))
