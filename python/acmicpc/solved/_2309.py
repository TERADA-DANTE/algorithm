from itertools import combinations
numbers = [int(input()) for _ in range(9)]


def solution(numbers):
    queue = list(combinations(numbers, 7))
    while queue:
        candidates = queue.pop()
        if sum(candidates) == 100:
            return '\n'.join(list(map(str, sorted(candidates))))


print(solution(numbers))
