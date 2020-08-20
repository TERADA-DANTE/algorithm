a, b = list(map(int, input().split()))
n = int(input())


def solution(a, b, n):
    [numbers, number] = [list(map(int, input().split())), 0]
    for i in range(n):
        number += numbers[i] * a**(n-1-i)
    numbers = []
    while number >= b:
        numbers.append(number % b)
        number //= b
    numbers.append(number)
    return ' '.join(map(str, numbers[::-1]))


print(solution(a, b, n))
