n = int(input())
numbers = list(enumerate(map(int, input().split())))
newNumbers = sorted(
    enumerate(sorted(numbers, key=lambda v: v[1])), key=lambda v: v[1][0])
print(*[i for i, v in newNumbers])
