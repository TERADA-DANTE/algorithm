import sys
sys.setrecursionlimit(10000)
a, b, c = list(map(int, input().split()))


def solution(a, b, c):
    def execute(x, b, c):
        global a
        if not b:
            return x
        if x % c == (x*a) % c:
            return x % c
        return execute(x*a, b-1, c)
    return execute(a, b, c)


print(solution(a, b, c))
