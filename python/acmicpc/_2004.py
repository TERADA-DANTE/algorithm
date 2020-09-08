n, m = list(map(int, input().split()))


def getNumbers(n, i, cnt=0, j=1):
    while i**j <= n:
        cnt += n//(i**j)
        j += 1
    return cnt


def execute(n, m, i):
    return getNumbers(n, i) - getNumbers(n-m, i) - getNumbers(m, i)


def solution(n, m):
    return min(execute(n, m, 2), execute(n, m, 5))


print(solution(n, m))
