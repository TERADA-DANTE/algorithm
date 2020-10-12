cnt = {0: 0, 1: 0}


def isValid(arr, n):
    for i in range(n):
        if len(set(arr[i])) != 1:
            return False
    return True


def partition(arr, n):
    return [[arr[0+i+a][0+b:n+b] for i in range(n)] for a, b in [[0, 0], [0, n], [n, 0], [n, n]]]


def solution(arr):
    execute(arr, len(arr))
    return list(cnt.values())


def execute(arr, l):
    if not isValid(arr, l):
        for particle in partition(arr, int(l//2)):
            execute(particle, int(l//2))
    else:
        cnt[arr[0][0]] += 1


print(solution([[1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 1, 1, 1],
                [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))
