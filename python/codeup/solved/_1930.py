while True:
    try:
        k, n = list(map(int, input().split()))
        dp = [i for i in range(n+1)]
        for _ in range(k):
            for i in range(n+1):
                dp[i] = 0 if not i else dp[i]+dp[i-1]
        print(dp[n])
    except EOFError:
        break
