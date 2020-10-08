from itertools import permutations
n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]


def sum(arr):
    result = 0
    for i in range(n):
        result += costs[i][arr[i]]
    return result


def dfs(row, col, h):
    global answer
    if row == n-1:
        answer = max(answer, sum(h))
        return
    else:
        for i in range(n):
            if i not in h:
                dfs(row+1, col, h+[i])


answer = 0
for i in range(n):
    dfs(0, i, [i])
print(answer)
