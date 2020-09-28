n = int(input())
dec = [i for i in range(10)]
twl = [chr(i+65) for i in range(12)]
d = str(dec[n % 10 - 4])
t = str(twl[n % 12 - 4])
# 3 4 5 6 7 8 9 0 1
# 9 0 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6 7 8 9 10 11
# F  G  H
# A B C D E F
print(t+d)
