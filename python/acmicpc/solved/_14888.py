from collections import deque
from itertools import permutations, combinations
[n, s] = [int(input()), '']
numbers = list(map(int, input().split()))

for sign, i in zip(['+', '-', '*', '/'], list(map(int, input().split()))):
    s += sign*i


def execute(numbers, operations):
    numbers = deque(numbers)
    operations = deque(operations)
    initial = numbers.popleft()
    while numbers:
        number = numbers.popleft()
        operation = operations.popleft()
        if operation == '+':
            initial += number
        elif operation == '-':
            initial -= number
        elif operation == '*':
            initial *= number
        else:
            if initial >= 0:
                initial = initial//number
            else:
                initial = -1 * ((-1 * initial) // number)
    return initial


def solution(n, numbers, operators):
    results = [execute(numbers, operations)
               for operations in permutations(operators, n-1)]
    return '\n'.join(list(map(str, [max(results), min(results)])))


print(solution(n, numbers, list(s)))
