import sys
input = sys.stdin.readline
n = int(input())
d = dict()
numbers = list(map(int, input().split()))
for number in numbers:
    d[number] = True
m = int(input())
candidates = list(map(int, input().split()))


def isInclude(n):
    if d.get(n):
        return 1
    else:
        return 0


def solution(numbers):
    answer = [None] * m
    for i in range(m):
        answer[i] = isInclude(candidates[i])
    return ' '.join(map(str, answer))


print(solution(numbers))
