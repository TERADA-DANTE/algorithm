n = int(input())
i = 0
stack = []
while len(str(bin(i))[2:]) <= n:
    stack.append(str(bin(i))[2:].rjust(n, '0'))
    i += 1
for i in range(len(stack)):
    print(stack[i].replace('0', 'O').replace('1', 'X'))
