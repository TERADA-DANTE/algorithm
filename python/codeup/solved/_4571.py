m = int(input())
n = int(input())
i = 1
numbers = []
while i**2 <= n:
    if m <= i**2:
        numbers.append(i**2)
    i += 1
print(sum(numbers))
print(numbers[0])
