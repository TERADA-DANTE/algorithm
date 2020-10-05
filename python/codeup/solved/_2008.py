n = int(input())
numbers = list(map(int, input().split()))

ascending = sorted(numbers)
descending = sorted(numbers, reverse=1)

flag = False
if len(set(numbers)) == 1:
    print('섞임')
else:
    for i in range(n):
        if numbers[i] != ascending[i]:
            break
    else:
        flag = True
        print('오름차순')
    for i in range(n):
        if numbers[i] != descending[i]:
            break
    else:
        flag = True
        print('내림차순')
    if not flag:
        print('섞임')
