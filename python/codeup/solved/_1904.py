a, b = list(map(int, input().split()))


def solution(a, b):
    if a > b:
        return
    elif a % 2:
        print(a)
        solution(a+2, b)
    else:
        solution(a+1, b)


solution(a, b)
