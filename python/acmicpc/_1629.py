
a, b, c = list(map(int, input().split()))


def solution(a, b, c):
    result = a
    series = []
    while b != 1:
        series.append(b)
        if b % 2:
            b -= 1
        else:
            b = int(b//2)
    while series:
        s = series.pop()
        if s % 2:
            result = (result * a) % c
        else:
            result = (result ** 2) % c
    return result % c


print(solution(a, b, c))
