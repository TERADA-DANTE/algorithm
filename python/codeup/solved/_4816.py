t = int(input())
arr = [300, 60, 10]
answer = [0, 0, 0]
i = 0
while t and arr:
    n = arr.pop(0)
    if int(t//n):
        answer[i] = int(t//n)
        t = t % n
    i += 1
if t:
    print(-1)
else:
    print(*answer)
