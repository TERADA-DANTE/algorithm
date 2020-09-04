answer = []


def getSum(arr1, arr2):
    return list(map(sum, zip(arr1, arr2)))


def solution(n):
    dp = [[1, 0], [0, 1]]
    for i in range(2, n+1):
        dp.append(getSum(dp[i-1], dp[i-2]))
    return dp[n]


for _ in range(int(input())):
    answer.append(solution(int(input())))

for a in answer:
    print(*a)
