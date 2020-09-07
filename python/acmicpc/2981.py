n = int(input())
numbers = [int(input()) for _ in range(n)]

# mathematical theory required


def solution(n, numbers):
    2 4 28
    h = []
    for i in range(2, max(numbers)):
        if len(set([number % i for number in numbers])) == 1:
            h.append(i)
    return ' '.join(list(map(str, h)))
 1 2 3  6
 1 2 17 34 
 1 2 19 38 



print(solution(n, numbers))
