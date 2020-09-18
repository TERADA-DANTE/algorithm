s = input().lower()
for i in range(1, 16):
    print(str(s).upper() + '*' + str(hex(i))[2:].upper() +
          '=' + str(hex(int(s, 16)*i))[2:].upper())
