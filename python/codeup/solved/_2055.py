
from itertools import combinations
a, b = list(map(int, input().split()))


def primize(n, i=2):
    h = [1]
    while n != 1:
        if not n % i:
            h.append(i)
            n = int(n//i)
        else:
            i += 1
    return h


def mul(tuples):
    result = 1
    for i in range(len(tuples)):
        result *= tuples[i]
    return result


def getSet(arr):
    result = set()
    for i in range(1, len(arr)+1):
        l = list(map(lambda v: mul(v), combinations(arr, i)))
        for e in l:
            result.add(e)
    return result


print(*sorted(getSet(primize(a)) | getSet(primize(b))))
