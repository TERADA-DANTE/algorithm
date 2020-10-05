from itertools import combinations
budget = int(input())
n = int(input())
costs = list(map(int, input().split()))
answer = 0
for i in range(1, n+1):
    l = list(filter(lambda v: v <= budget, list(
        map(sum, combinations(costs, i)))))
    answer = max(max(l if l else [0]), answer)
print(answer)
