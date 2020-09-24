n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [abs(a[i]-b[i]) for i in range(n)]
m = c.index(min(c))
d = [False, False]
s = 0
for i in range(n):
    if i != m:
        if a[i] > b[i]:
            d[0] = True
            s += a[i]
        else:
            d[1] = True
            s += b[i]
if not d[0]:
    s += a[m]
elif not d[1]:
    s += b[m]
else:
    s += max(a[m], b[m])
print(s)
