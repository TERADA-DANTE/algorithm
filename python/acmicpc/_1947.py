n = int(input())


def solution(n):
    numbers = [None, 0, 1] + [None]*(n-2)
    if n == 1:
        return 0
    elif n == 2:
        return 1
    for i in range(3, n+1):
        numbers[i] = ((i-1) * (numbers[i-1] + numbers[i-2])) % 1000000000
    return numbers[-1] % 1000000000


print(solution(n))
