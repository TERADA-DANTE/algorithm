a, b, c, n = list(map(int, input().split()))


def solution():
    for i in range(int(n//a)+1):
        for j in range(int(n//b)+1):
            for k in range(int(n//c)+1):
                if a*i+b*j+c*k == n:
                    return 1
    return 0


print(solution())
