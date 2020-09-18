n, m = list(map(int, input().split()))

d = dict()
for _ in range(n):
    s, k = input().split()
    if d.get(s):
        d[s].append(int(k))
    else:
        d[s] = [int(k)]
answer = dict()
for key in d.keys():
    answer[key] = sum(d[key])

for _ in range(m):
    s = input()
    if answer.get(s):
        print(answer[s])
    else:
        print(0)
