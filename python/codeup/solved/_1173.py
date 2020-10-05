hour, minute = list(map(int, input().split()))
if minute-30 >= 0:
    print(hour, minute-30)
else:
    hour -= 1
    minute -= 30
    minute += 60
    if hour < 0:
        hour += 24
    print(hour, minute)
