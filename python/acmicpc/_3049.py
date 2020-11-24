n = int(input())

fibos = [1, 1, 2]
for i in range(n-2):
    fibos.append(fibos[-1]*(i+3))


def combination(n, k):
    return int(fibos[n] / (fibos[k] * fibos[n-k]))


def solution():
    return combination(n, 4)


print(solution())
