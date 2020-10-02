n = int(input())
cnt = 0


def solution(n, chk=1):
    global cnt
    if n:
        if chk:
            solution(n-1, 0)
            solution(n-1, 1)
        else:
            solution(n-1, 1)
    else:
        cnt += 1
        return


if n == 1:
    print(2)
else:
    solution(n)
    print(cnt)
