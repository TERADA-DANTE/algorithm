n = input()
numbers = list(map(str, input().split()))


def solution(n, numbers):
    ret = 0
    for number in numbers:
        if number[-1] == n:
            ret += 1
    return ret


print(solution(n, numbers))
