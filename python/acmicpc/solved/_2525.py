hour, min = list(map(int, input().split()))
time = int(input())
h, m = time//60, time % 60
min += m
if 60 <= min:
    hour += 1
min = min % 60
hour += h
if 24 <= hour:
    hour = hour % 24
print(hour, min)
