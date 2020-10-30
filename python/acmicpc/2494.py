from collections import deque
n = int(input())
initial = int(input())
target = int(input())


def solution(n, initial, target):
    dp = [0] * ((9*10**(n-1))+1)
    queue = [[0, initial]]


print(solution(n, initial, target))
