n = int(input())
factorials = [1, 1]
for i in range(29):
    factorials.append(factorials[-1] * (i+2))


def combination(n, k):
    return int(factorials[n] / (factorials[n-k] * factorials[k]))
    # nCk = n! / n-k! * k!


for _ in range(n):
    k, n = list(map(int, input().split()))
    print(combination(n, k))
