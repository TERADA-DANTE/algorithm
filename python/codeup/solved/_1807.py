a, b = list(map(int, input().split()))
d = {1: 1}


def rain(n, cnt=0):
    if d.get(n):
        return cnt+d[n]
    elif n == 1:
        return cnt
    elif n % 2:
        return rain(3*n+1, cnt+1)
    elif not n % 2:
        return rain(int(n//2), cnt+1)


for i in range(2, b+1):
    d[i] = rain(i)
candidates = [(i, d[i]) for i in range(a, b+1)]
print(*sorted(candidates, key=lambda v: (-v[1], v[0]))[0])
# 1 1
# 2 1
# 3 10 5 16 8 4 2 1
# 4 2 1
# 5 16 8 4 2 1
# 6 3 10 5 16 8 4 2 1
# 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
