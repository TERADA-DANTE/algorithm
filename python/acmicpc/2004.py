import re
n, m = list(map(int, input().split()))


def separate(s, c):
    if float(s) % 1 == 0:
        s = str(int(float(s)))
        t = re.search(r'0+$', s)
        if t:
            return [int(s[:-len(t.group())]), c + len(t.group())]
        return [int(s), c]
    else:
        t = len(s) - s.index('.') - 1
        return [int(float(s) * (10**t)), c-t]


def solution(n, m):
    initial = separate(str(n), 0)
    for i in range(1, m):
        initial = separate(str(initial[0] * (n-i) / (i+1)), initial[1])
    return initial[-1]


print(solution(n, m))
