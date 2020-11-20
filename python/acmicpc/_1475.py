numbers = list(map(int, list(input())))

# 6, 9 가 아닌 경우 한 세트가 필요하다.
check = [0] * 10
limit = 1
for number in numbers:
    if check[number] < limit:
        check[number] += 1
    else:
        if number == 6:
            if check[9] < limit:
                check[9] += 1
            else:
                limit += 1
                check[number] += 1
        elif number == 9:
            if check[6] < limit:
                check[6] += 1
            else:
                limit += 1
                check[number] += 1
        else:
            limit += 1
            check[number] += 1
print(limit)


# 2 4 4 6 5
# 2 4 6 6 5
# 2 4 6 9 5
# 리버셋 3개 => 6 9 6 9
# 이리버 2개
