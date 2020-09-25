from math import gcd

a, b, c = list(map(int, input().split()))
d = gcd(a, b)
print(gcd(c, d))
