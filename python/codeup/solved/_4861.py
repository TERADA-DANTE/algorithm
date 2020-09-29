import math
n, k = list(map(int, input().split()))
students = [list(map(int, input().split())) for _ in range(n)]
males = [0] * 6
females = [0] * 6
for sex, grade in students:
    if sex:
        males[grade-1] += 1
    else:
        females[grade-1] += 1
answer = 0
for male in males:
    answer += math.ceil(male/k)
for female in females:
    answer += math.ceil(female/k)
print(answer)
