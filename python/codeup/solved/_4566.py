m = int(input())
n = int(input())
cnt = 0
primes = [False, False, True, True] + [None] * (n-3)


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if not n % i:
            return False
    return True


for i in range(4, n+1):
    primes[i] = isPrime(i)


numbers = [i for i in range(m, n+1) if primes[i]]
print(sum(numbers))
print(numbers[0])
