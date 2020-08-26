n = int(input())


def star(n):
    if n == 3:
        return '*'
    return [star(n//2), star(n//2), blank(n//2), star(n//2)]


def blank(n):
    if n == 3:
        return ' '
    return blank(n//2)


def solution(n):
    return [star(n), star(n), blank(n), star(n)]


print(solution(n))
