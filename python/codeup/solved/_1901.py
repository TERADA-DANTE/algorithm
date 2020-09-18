n = int(input())


def solution(i):
    global n
    if n+1 != i:
        print(i)
        solution(i+1)


solution(1)
