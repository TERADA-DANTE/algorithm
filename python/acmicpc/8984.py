import sys
input = sys.stdin.readline
n, l = list(map(int, input().split()))
lines = [list(map(int, input().split())) for _ in range(n)]


def solution(n, l, lines):
    return n, l, lines


print(n, l, lines)
