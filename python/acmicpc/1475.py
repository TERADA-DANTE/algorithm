numbers = list(input())

irreverable = 0
reverable = 0
# 6, 9 가 아닌 경우 한 세트가 필요하다.
for i in range(len(numbers)):
    if numbers[i] not in [6, 9]:
        irreverable += 1
    else:
        reverable += 1
