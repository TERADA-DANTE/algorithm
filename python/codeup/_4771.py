plates = input()

dp = []
for i in range(len(plates)):
    if not i:
        dp.append(10)
    else:
        dp.append(
            5 if plates[i] == plates[i-1] else 10
        )
print(sum(dp))
