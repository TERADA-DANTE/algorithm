s = 0
n = int(input())
for i in range(1, 100):
    s += i
    if s >= n:
        print(i)
        break
