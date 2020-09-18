n = int(input())
series = [list(map(int, input().split())) for _ in range(n)]
series.sort(key=lambda v: v[0])
for i in range(n):
    print(*series[i])
