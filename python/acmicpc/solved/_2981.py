import sys
input = sys.stdin.readline
n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()
x = float('inf')


def divisors(n):
    h = []
    for i in range(2, n+1):
        if not n % i:
            h.append(i)
    return h


for i in range(n-1):
    if x > abs(numbers[i+1]-numbers[i]):
        x = abs(numbers[i+1]-numbers[i])
candidates = divisors(x)


def solution(candidates, numbers):
    answer = []
    for candidate in candidates:
        check = set()
        for number in numbers:
            check.add(number % candidate)
            if len(check) > 1:
                break
        else:
            answer.append(candidate)

    return answer


print(*solution(candidates, numbers))
