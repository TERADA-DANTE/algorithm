from collections import deque
n, m = list(map(int, input().split()))
days = [1] * (n+1)
if m:
    xs = list(map(int, input().split()))
    for x in xs:
        days[x] = 0
answer = float('inf')
# day, coupon, history


def cal(arr, result=0):
    for v in arr:
        if v == 5:
            result += 37000
        elif v == 3:
            result += 25000
        elif v == 1:
            result += 10000
    return result


13 5 2
3
0 0 0 0 0
0 0 0 0 1
0 0 1 1 0
0 1 1 1 0
1 1 1 1 0
1 1 1 1 1


def solution(day, coupon, history):
    global answer
    if day+1 > n:
        answer = min(answer, cal(history))
        return
    elif days[day+1] and day+1 <= n:
        if coupon >= 3:
            solution(day+1, coupon-3, history)
        else:
            solution(day+5, coupon+2, history+[5])
            solution(day+3, coupon+1, history+[3])
            solution(day+1, coupon, history+[1])
    elif not days[day+1]:
        solution(day+1, coupon, history)


solution(0, 0, [])
print(answer)
