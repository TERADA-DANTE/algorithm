n = int(input())
coins = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
cnt = 0
while coins and n:
    coin = coins.pop()
    if int(n//coin):
        cnt += int(n//coin)
        n = n % coin
print(cnt)
