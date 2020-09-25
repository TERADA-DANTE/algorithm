hours, minutes, seconds = list(map(int, input().split()))
time = int(input())
if time >= 3600:
    hours += time//3600
    time = time % 3600
if time >= 60:
    minutes += time//60
    time = time % 60
seconds += time

if seconds >= 60:
    minutes += 1
    seconds -= 60
if minutes >= 60:
    minutes -= 60
    hours += 1
if hours >= 24:
    hours = hours % 24
print(hours, minutes, seconds)
