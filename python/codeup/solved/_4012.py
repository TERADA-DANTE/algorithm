n = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    cnt = 0
    for n in numbers:
        if n > number:
            cnt += 1
    print(number, cnt+1)
