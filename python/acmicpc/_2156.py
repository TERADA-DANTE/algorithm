n = int(input())

drinks = [int(input()) for _ in range(n)]


def solution(n, drinks):
    if n < 3:
        return sum(drinks)
    dp = [drinks[0], drinks[1]+drinks[0],
          max([drinks[1] + drinks[0], drinks[2] + drinks[0], drinks[1] + drinks[2]])]
    for i in range(3, n):
        dp.append(max(dp[i-3]+drinks[i] + drinks[i-1],
                      dp[i-2] + drinks[i], dp[i-1]))
    return max(dp)


print(solution(n, drinks))
