n, m, t, k = list(map(int, input().split()))
arr = []
for i in range(t):
    C, r = list(map(int, input().split()))
    arr.append((m-r, C))


def solution(n, m, t, k, arr):
    jewels = set()
    for i in range(t):
        r, c = arr[i]
        jewels.add((r, c))
        for j in range(i+1, t):
            R, C = arr[j]
            jewels.add((r, C))
            jewels.add((R, c))
    answer = 0
    for row, col in jewels:
        if row+k > m:
            row = m-k
        if col+k > n:
            col = n-k
        l = len([None for r, c in arr if row <=
                 r <= row+k and col <= c <= col+k])
        if answer < l:
            answer = l
            C = col
            R = m-row
    return f'{C} {R}\n{answer}'


print(solution(n, m, t, k, arr))
