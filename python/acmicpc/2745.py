import math
n, b = input().split()


def solution(n, b):
    d = dict()
    for i in range(36):
        if i < 10:
            d[i] = i
        else:
            d[chr(i+55)] = i
    numbers = list(n)[::-1]
    answer = 0
    for i in range(len(numbers)):
        answer += math.pow(int(b), i) * \
            d[int(numbers[i]) if numbers[i].isdigit() else numbers[i]]
    return int(answer)


print(solution(n, b))
