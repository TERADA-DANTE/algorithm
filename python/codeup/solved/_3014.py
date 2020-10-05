n = int(input())
numbers = list(map(int, input().split()))
check = [0] * 100001
answer = []
for i in range(n):
    check[numbers[i]] += 1

for i in range(100001):
    if check[i]:
        for j in range(check[i]):
            answer.append(i)
print(*answer)
