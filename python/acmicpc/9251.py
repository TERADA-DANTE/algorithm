import sys
sys.setrecursionlimit(100000)
a = input()
b = input()
answer = 0


def solution(a, b, cnt, flag=False):
    global answer
    if flag:
        return
    if not a or not b:
        flag = True
        answer = cnt
        return
    elif a[-1] == b[-1]:
        return solution(a[:-1], b[:-1], cnt+1)
    elif a[0] == b[0]:
        return solution(a[1:], b[1:], cnt + 1)
    else:
        x = solution(a[:-1], b, cnt)
        y = solution(a, b[:-1], cnt)
        return max(x, y)


print(solution(a, b, 0))
