import sys
sys.setrecursionlimit(100000)
n, k = list(map(int, input().split()))


def solution(n, k):
    d = dict()

    def binomial(n, k):
        if d.get(f'{n}C{k}') or d.get(f'{n}C{n-k}'):
            return d[f'{n}C{k}']
        if k == 1 or n-k == 1:
            d[f'{n}C{k}'] = d[f'{n}C{n-k}'] = n
            return d[f'{n}C{k}']
        if n == k:
            d[f'{n}C{k}'] = d[f'{n}C{n-k}'] = 1
            return d[f'{n}C{k}']
        d[f'{n}C{k}'] = d[f'{n}C{n-k}'] = binomial(
            n-1, k) % 10007 + binomial(n-1, k-1) % 10007
        return d[f'{n}C{k}'] % 10007

    return binomial(n, k)


print(solution(n, k))
