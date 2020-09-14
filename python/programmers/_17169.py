def solution(numbers):
    result = set()
    while numbers:
        n = numbers.pop()
        for number in numbers:
            result.add(n + number)
    return list(result)


print(solution([5, 0, 2, 7]))
