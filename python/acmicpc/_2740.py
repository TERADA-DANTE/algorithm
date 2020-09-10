n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
x, y = list(map(int, input().split()))
b = [list(map(int, input().split())) for _ in range(x)]


def mul(tuple):
    return tuple[0] * tuple[1]


def solution(a, b, n, m, x, y):
    matrix = []
    for i in range(n):
        temp = []
        for j in range(y):
            temp.append(sum(map(mul, zip(a[i], b[j]))))
        matrix.append(' '.join(list(map(str, temp))))
    return '\n'.join(matrix)


print(solution(a, list(zip(*b)), n, m, x, y))
