numbers = list(map(int, input().split()))


def solution(numbers):
    return sum(map(int, [str(numbers[0])+str(numbers[1]), str(numbers[2])+str(numbers[3])]))


print(solution(numbers))
