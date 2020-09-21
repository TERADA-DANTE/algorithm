a, b, c = list(map(int, input().split()))
for i in range(1, min(a, b, c)+1):
    if not any([a % i, b % i, c % i]):
        x = i

print(x)
