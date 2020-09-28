from math import gcd
n, m = list(map(int, input().split()))
numbers = [i for i in range(n, m+1)]

d = dict()


def convert(a, b):
    g = gcd(a, b)
    return str(int(a/g)) + '/' + str(int(b/g))


for number in numbers:
    angles = [convert(1 * (j+1), number) for j in range(int(number//2))]
    for angle in angles:
        if not d.get(angle):
            d[angle] = True
print(len(d)*2)
