n = int(input())
m = 0
numbers = list(map(int, input().split()))


def getSum(numbers):
    return sum([abs(numbers[i]-numbers[i+1]) for i in range(len(numbers)-1)])


def solution(numbers):
    getSum(numbers)


print(solution(numbers))
