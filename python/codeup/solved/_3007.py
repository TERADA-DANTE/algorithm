n, m = list(map(int, input().split()))
numbers = list(map(int, input().split()))
questions = [list(map(int, input().split())) for _ in range(m)]
subSum = [numbers[0]]
for i in range(1, n):
    subSum.append(subSum[-1]+numbers[i])
for i in range(m):
    a, b = questions[i]
    if a == 1:
        print(subSum[b-1])
    else:
        print(subSum[b-1]-subSum[a-2])
