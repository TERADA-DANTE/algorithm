n = int(input())

d = dict()
for _ in range(n):
    code, number, name = input().split()
    if code == "I":
        if d.get(number):
            d[number].insert(0, name)
        else:
            d[number] = [name]
    else:
        if d.get(number):
            d[number].pop(0)
            if not d[number]:
                del d[number]
t = []
for i, v in sorted(d.items(), key=lambda v: int(v[0])):
    if len(v) > 1:
        for s in v:
            t.append([i, s])
    else:
        t.append([i, v[0]])
for i in map(int, input().split()):
    print(t[i-1][0], t[i-1][1])
