import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
a = input()
b = input()


def solution(a, b, cnt, flag=False):
    if flag:
        return cnt
    if not a or not b:
        flag = True
        return cnt
    elif a[-1] == b[-1]:
        return solution(a[:-1], b[:-1], cnt+1)
    elif a[0] == b[0]:
        return solution(a[1:], b[1:], cnt + 1)
    else:
        return max(solution(a[:-1], b, cnt), solution(a, b[:-1], cnt))


print(solution(a, b, 0))
