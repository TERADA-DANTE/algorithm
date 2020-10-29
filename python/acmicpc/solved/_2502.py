d, k = list(map(int, input().split()))


def solution(d, k):
    fibo = [None] * (d+1)
    fibo[1] = ['X']
    fibo[2] = ['Y']
    for i in range(3, d+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    x = fibo[d].count('X')
    y = fibo[d].count('Y')
    i, j = 1, 1
    while True:
        if x*i+j*y < k:
            j += 1
        elif x*i+j*y > k:
            i += 1
            j = 1
        else:
            return str(i) + '\n' + str(j)


print(solution(d, k))
