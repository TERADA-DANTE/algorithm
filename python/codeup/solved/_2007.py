n = int(input())
numbers = list(map(int, input().split()))

if n == 2:
    print('오름차순') if numbers[1] - numbers[0] > 0 else print('내림차순')
else:
    flag = numbers[1] - numbers[0] > 0
    for i in range(1, n):
        if (numbers[i]-numbers[i-1] > 0) != flag:
            print('섞임')
            break
    else:
        print('오름차순') if flag else print('내림차순')
