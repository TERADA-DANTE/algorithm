numbers = 0
answer = 0
for _ in range(10):
    out, inn = list(map(int, input().split()))
    numbers -= out
    numbers += inn
    answer = max(answer, numbers)
print(answer)
