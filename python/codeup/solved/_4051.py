total = 0
for i in range(5):
    start, end = list(map(float, input().split()))
    time = end-start
    time = time - 1 if time >= 1 else 0
    time = time if time <= 4 else 4
    total += time
if total >= 15:
    print(int(total*0.95*10000))
elif total <= 5:
    print(int(total*1.05*10000))
else:
    print(int(total*10000))
