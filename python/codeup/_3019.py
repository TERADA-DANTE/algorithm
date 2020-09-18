n = int(input())
data = [input().split() for _ in range(n)]
data.sort(key=lambda v: (int(v[1]), int(v[2]), int(v[3]), v[0]))
for i in range(n):
    print(data[i][0])
