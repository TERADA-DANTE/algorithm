from itertools import permutations
n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
orders = list(permutations(range(n), n))
answer = 0

for order in orders:
    result = 0
    for i in range(n):
        result += costs[i][order[i]]
    answer = max(answer, result)
print(answer)
# 3 1 4 2
# 2 5 4 3
# 1 4 1 2
# 2 5 4 3
