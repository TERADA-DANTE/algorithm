n = int(input())
numbers = [float(input()) for _ in range(n)]


def solution(n, numbers):
    answer = 0
    for i in range(n):
        result = 1
        while i >= 0:
            result *= numbers[i]
            i -= 1
            answer = max(answer, result)
    return '%.3f' % float(answer)


print(solution(n, numbers))
