numbers = []
d = dict()
for _ in range(10):
    numbers.append(int(input()))
for number in numbers:
    if d.get(number):
        d[number] += 1
    else:
        d[number] = 1
print(int(sum(numbers)/10))
print(sorted(list(d.items()), key=lambda v: -v[1])[0][0])
