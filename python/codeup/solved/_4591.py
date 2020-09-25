numbers = []
for _ in range(9):
    numbers.append(int(input()))
a = sorted(enumerate(numbers, start=1), key=lambda v: -v[1])[0]
print(a[1])
print(a[0])
