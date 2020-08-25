import sys
input = sys.stdin.readline
n = int(input())
d = dict()
numbers = list(map(int, input().split()))
for number in numbers:
    if d.get(number):
        d[number] += 1
    else:
        d[number] = 1
m = int(input())
candidates = list(map(int, input().split()))


def isInclude(n):
    if d.get(n):
        return d[n]
    else:
        return 0


def solution(numbers):
    answer = [None] * m
    for i in range(m):
        answer[i] = isInclude(candidates[i])
    return ' '.join(map(str, answer))


print(solution(numbers))
