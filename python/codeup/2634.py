n = int(input())
t = int(input())
coins = list(map(int, input().split()))
dp = [None] * t


def solution(i, cnt=0):
    target = n
    newCoins = coins[0:i]
    while target:
        coin = newCoins.pop()
        if target//coin:
            cnt += target//coin
            target = target % coin
    return cnt


for i in range(t):
    dp[i] = solution(t-i)

print(dp)
