m = int(input())
n = int(input())
cnt = 0


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, i):
        if not n % i:
            return False
    return True


for i in range(n, m+1):
    if isPrime(i):
        cnt += 1

print(cnt if cnt else -1)
