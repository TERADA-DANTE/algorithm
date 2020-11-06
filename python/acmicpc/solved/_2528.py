import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, l = list(map(int, input().split()))
lines = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')


def index(floor, time):
    length, direction = lines[floor]
    mid = int((length+1)//2)
    c = l-mid*2
    t = int(time//c) if c else -1
    if t < 0:
        return mid
    if t % 2:
        return mid+time % c if direction else l-mid-time % c
    return l-mid-time % c if direction else mid+time % c


def solution(n, l, floor, cnt):
    global answer
    if floor == n-1:
        return cnt
    for i in range(l):
        bottom = index(floor, cnt+i)
        b = int(lines[floor][0]//2)
        top = index(floor+1, cnt+i)
        t = int(lines[floor+1][0]//2)
        if not top+t < bottom-b and not bottom+b < top-t:
            return solution(n, l, floor+1, cnt+i)


print(solution(n, l, 0, 0))
