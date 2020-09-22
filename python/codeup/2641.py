n = int(input())
cnt = 0


def solution(total, chk):
    global cnt, n
    chk -= 1
    if n - total >= 1:
        solution(total+1, chk)
    if n - total >= 2:
        solution(total+2, chk)
    if n - total >= 3 and chk <= 0:
        solution(total+3, 3)
    if n-total == 0:
        cnt += 1
    else:
        return


solution(0, 0)
print(cnt)
