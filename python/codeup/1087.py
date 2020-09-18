n = int(input())
s = 0
for i in range(1, 10000000000):
    s += i
    if s >= n:
        print(s)
        break
