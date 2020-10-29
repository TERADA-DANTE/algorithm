numbers = [int(input()) for _ in range(7)]

odds = [number for number in numbers if number % 2]
if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)
