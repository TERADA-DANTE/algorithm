hours, minutes = list(map(int, input().split()))
time = int(input())
if time >= 60:
    hours += time//60
    time = time % 60
    minutes += time
else:
    minutes += time
if minutes >= 60:
    minutes -= 60
    hours += 1
if hours >= 24:
    hours -= 24
print(hours, minutes)
