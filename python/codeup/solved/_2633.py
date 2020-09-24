n, k = list(map(int, input().split()))

numbers = list(map(int, input().split()))

for i in range(n):
    if numbers[i] >= k:
        print(i+1)
        break
else:
    print(i+2)
