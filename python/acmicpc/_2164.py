from collections import deque
n = int(input())

numbers = deque(list(range(1, n+1)))


def solution(numbers):
    while len(numbers) > 1:
        numbers.popleft()
        numbers.append(numbers.popleft())
    return numbers[0]


print(solution(numbers))
