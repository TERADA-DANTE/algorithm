n = int(input())

scores = [input().split() for _ in range(n)]

scores.sort(key=lambda v: -int(v[1]))
name = scores[0][0]
a = int(scores[0][2])
b = int(scores[0][3])
c = 0
d = 0
for i in range(n):
    if int(scores[i][2]) > a:
        c += 1

for i in range(n):
    if int(scores[i][3]) > b:
        d += 1
print(name, c+1, d+1)
