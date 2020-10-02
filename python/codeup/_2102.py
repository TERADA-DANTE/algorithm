n = int(input())
i = 1
while True:
    m = int(str(bin(i))[2:])
    if m > 18446744073709551615:
        print(0)
        break
    else:
        if not m % n:
            print(m)
            break
        i += 1
