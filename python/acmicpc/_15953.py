t = int(input())


def A(a):
    if not a:
        return 0
    if a <= 1:
        return 5000000
    if a <= 3:
        return 3000000
    if a <= 6:
        return 2000000
    if a <= 10:
        return 500000
    if a <= 15:
        return 300000
    if a <= 21:
        return 100000
    else:
        return 0


def B(b):
    if not b:
        return 0
    if b <= 1:
        return 5120000
    if b <= 3:
        return 2560000
    if b <= 7:
        return 1280000
    if b <= 15:
        return 640000
    if b <= 31:
        return 320000
    else:
        return 0


def solution(a, b):
    return A(a) + B(b)


answer = []
for _ in range(t):
    a, b = list(map(int, input().split()))
    answer.append(str(solution(a, b)))
print('\n'.join(answer))
