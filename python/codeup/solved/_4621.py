n, k = list(map(int, input().split()))
numbers = []
for i in range(1, n+1):
    if not n % i:
        numbers.append(i)
print(numbers[k-1] if len(numbers) >= k else 0)
