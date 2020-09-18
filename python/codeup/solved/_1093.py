serires = [None] + [0] * 23
_ = int(input())
numbers = list(map(int, input().split()))

while numbers:
    number = numbers.pop()
    serires[number] += 1

print(*serires[1:])
