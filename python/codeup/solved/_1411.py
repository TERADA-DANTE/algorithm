n = int(input())
cards = [None] + [0] * n
for _ in range(n-1):
    i = int(input())
    cards[i] += 1
for i in range(1, n+1):
    if not cards[i]:
        print(i)
        break
