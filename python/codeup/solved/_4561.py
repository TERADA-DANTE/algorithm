numbers = []
for _ in range(7):
    numbers.append(int(input()))
odds = sorted([number for number in numbers if number % 2])
print(sum(odds))
print(odds[0])
