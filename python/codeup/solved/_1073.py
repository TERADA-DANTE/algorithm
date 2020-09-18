numbers = list(map(int, input().split()))

while numbers:
    number = numbers.pop(0)
    if not number:
        break
    print(number)
