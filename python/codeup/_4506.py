from math import gcd
a, b = list(map(int, input().split()))
print(gcd(a, b))
print(int(a*b/gcd(a, b)))
