def solution(numbers):
    SEX = set()
    while numbers:
        n = numbers.pop()
        for number in numbers:
            SEX.add(n + number)
    return list(sorted(SEX))


print(solution([5, 0, 2, 7]))
