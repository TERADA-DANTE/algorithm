import math
n = int(input())
numbers = list(map(int, input().split()))


def solution(n, numbers):
    answer = []
    for i in range(1, n):
        g = math.gcd(numbers[0], numbers[i])
        answer.append(f'{int(numbers[0]//g)}/{int(numbers[i]//g)}')
    return '\n'.join(answer)


print(solution(n, numbers))
