arr = ['', '', '']
string = list(input())
i = 0
while string:
    s = string.pop(0)
    if s == '.':
        i += 1
        continue
    arr[i] += s
print(arr[2].rjust(2, '0') + '-' +
      arr[1].rjust(2, '0') + '-'+arr[0].rjust(4, '0'))
