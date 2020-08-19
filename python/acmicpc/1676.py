n = int(input())


def factorial(n):
    numbers = [1, 1] + [None]*(n-1)
    for i in range(2, n+1):
        numbers[i] = numbers[i-1] * i
    return numbers


def solution(n):
    f = factorial(n)
    cnt = 0
    for s in str(f[-1])[::-1]:
        if int(s):
            return cnt
        else:
            cnt += 1


print(solution(n))
