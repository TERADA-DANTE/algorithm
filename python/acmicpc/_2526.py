n, p = list(map(int, input().split()))


def solution(n, p):
    arr = [n]
    while True:
        i = (arr[-1]*arr[0]) % p
        if i in arr:
            return len(arr) - arr.index(i)
        else:
            arr.append(i)


print(solution(n, p))
