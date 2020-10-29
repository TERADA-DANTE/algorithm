n = int(input())
numbers = list(map(int, input().split()))


def solution(n, numbers):
    result = []
    for i in range(n):
        number = numbers[i]
        result.insert(len(result)-number, i+1)
    return result


print(*solution(n, numbers))
