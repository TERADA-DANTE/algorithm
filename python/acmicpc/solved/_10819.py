from itertools import permutations
n = int(input())
m = 0
numbers = list(map(int, input().split()))


def getSum(tuple):
    return sum([abs(tuple[i]-tuple[i+1]) for i in range(len(tuple)-1)])


def solution(numbers):
    return max(list(map(getSum, permutations(numbers))))


print(solution(numbers))
