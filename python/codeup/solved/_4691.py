
n = int(input())
answer = 0


def solution(arr):
    a, b, c, d = arr
    if len(set(arr)) == 1:
        return 50000 + a*5000
    if a == b == c or a == b == d or a == c == d or b == c == d:
        return 10000 + arr[1]*1000
    if a == b and c == d or a == c and b == d or a == d and b == c:
        return 2000 + 500*arr[0] + 500*arr[-1]
    if a == b or a == c or a == d or b == c or b == d or c == d:
        if arr.count(a) == 2:
            return 1000 + 100 * a
        if arr.count(b) == 2:
            return 1000 + 100 * b
        if arr.count(c) == 2:
            return 1000 + 100 * c
        if arr.count(d) == 2:
            return 1000 + 100 * d

    else:
        return max(arr) * 100


for _ in range(n):
    answer = max(answer, solution(sorted(map(int, input().split()))))

print(answer)
