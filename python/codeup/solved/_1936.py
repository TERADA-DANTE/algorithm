a, b = sorted(map(int, input().split()))
d = dict()


def solution(n, c=0):
    d[n] = c
    if n != 1:
        solution(int(n//2), c+1)
    return


def execute(n, c=0):
    if d.get(n):
        return d[n] + c
    return execute(int(n//2), c+1)


solution(b)
if a == b:
    print(0)
else:
    print(execute(a))
