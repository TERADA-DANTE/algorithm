def solution(numbers):
    n = numbers.count(1)
    if n == 4:
        return 'E'
    if n == 3:
        return 'A'
    if n == 2:
        return 'B'
    if n == 1:
        return 'C'
    if n == 0:
        return 'D'


for i in range(3):
    numbers = list(map(int, input().split()))
    print(solution(numbers))
