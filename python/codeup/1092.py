from math import gcd

a, b, c = list(map(int, input().split()))

k = int(a*b / gcd(a, b))
print(int(k*c / gcd(k, c)))
