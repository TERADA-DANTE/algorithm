import time
horizon, vertical = list(map(int, input().split()))

position = list(map(int, input().split()))

k = int(input())


def cal(time, length, offset):
    q = int(time+offset-1)//length
    r = (time+offset-1) % length
    return r+1 if not q % 2 else length-1-r


def solution(position, k):
    x, y = position
    return [cal(k, horizon, x), cal(k, vertical, y)]


#  5 6 7 8 9 10 11 12 13 14 15 16 17
#  1 2 3 4 5 6  7  8  9  10 11 12 13
#  5 6 5 4 3 2  1  0  1  2   3  4 5
#  4 5 6 5
print(*solution(position, k))
