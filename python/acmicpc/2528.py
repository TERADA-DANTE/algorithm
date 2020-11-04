import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
#n, l = list(map(int, input().split()))
n = 3000
l = 3000
# 재귀로 풀면 못푼다.
#lines = [list(map(int, input().split())) for _ in range(n)]
lines = [[2, 0] for _ in range(500)] + [[8, 1]
                                        for _ in range(2000)] + [[4, 0] for _ in range(500)]
answer = float('inf')
dp = [float('inf')] * n


def index(floor, time):
    length, direction = lines[floor]
    mid = int((length+1)//2)
    c = l-mid*2
    t = int(time//c)
    if t % 2:
        return mid+time % c if direction else l-mid-time % c
    return l-mid-time % c if direction else mid+time % c


def solution(n, l, floor, cnt):
    global answer
    print(floor, cnt, answer)
    length, direction = lines[floor]
    if dp[floor] <= cnt:
        return
    dp[floor] = cnt
    if floor == n-1:
        answer = min(answer, cnt)
        return
    if direction:
        for i in range(l):
            bottom = index(floor, cnt+i)
            top = index(floor+1, cnt+i)
            wing = int(lines[floor+1][0]//2)
            if not top+wing < bottom-int(length//2) and not bottom+int(length//2) < top-wing:
                solution(n, l, floor+1, cnt+i)
    else:
        for i in range(l):
            bottom = index(floor, cnt+i)
            top = index(floor+1, cnt+i)
            wing = int(lines[floor+1][0]//2)
            if not top+wing < bottom-int(length//2) and not bottom+int(length//2) < top-wing:
                solution(n, l, floor+1, cnt+i)


solution(n, l, 0, 0)
print(answer)
