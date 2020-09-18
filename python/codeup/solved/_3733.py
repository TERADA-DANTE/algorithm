a, b = list(map(int, input().split()))
check = dict()
answer = []
cnt = 0
idx = 0


def collatz(n, history=[]):
    if check.get(n):
        return len(history) + check[n]
    elif n == 1:
        return len(history) + 1
    elif n % 2:
        return collatz(n*3+1, history+[n])
    else:
        return collatz(int(n//2), history+[n])


for i in range(a, b+1):
    re = collatz(i)
    check[i] = re
    if cnt < re:
        cnt = re
        idx = i
print(idx, cnt)
