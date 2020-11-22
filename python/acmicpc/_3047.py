numbers = list(map(int, input().split()))
m = min(numbers)
M = max(numbers)
order = list(input())
d = dict()
while numbers:
    number = numbers.pop()
    if number == m:
        d['A'] = number
    elif number == M:
        d['C'] = number
    else:
        d['B'] = number
print(
    ' '.join([str(d[s]) for s in order])
)
