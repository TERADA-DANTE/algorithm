import time
n, k = list(map(int, input().split()))

s = time.time()
dp = [1, 1]
for i in range(2, n+2):
    dp.append(dp[-1]*i)
a = int((dp[n] / dp[n-k] / dp[k]) % 100000000)
print(time.time()-s)
s = time.time()
d = dict()