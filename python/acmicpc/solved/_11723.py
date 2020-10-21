import sys
inp = sys.stdin.readline
n = int(inp())
S = set()
for _ in range(n):
    a = inp().strip().split()
    if len(a) == 2:
        b = int(a[1])
    if a[0] == 'add':
        S.add(int(b))
    elif a[0] == 'remove' and b in S:
        S.remove(b)
    elif a[0] == 'check':
        if b in S:
            print(1)
        else:
            print(0)
    elif a[0] == 'toggle':
        if b in S:
            S.remove(b)
        else:
            S.add(b)
    elif a[0] == 'all':
        S = set(range(1, 21))
    elif a[0] == 'empty':
        S.clear()
