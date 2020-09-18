n = input()
arr = [None] * len(n)
for i in range(len(n)):
    arr[i] = int(n[i]) * 10**(len(n)-i-1)
print('\n'.join(list(map(lambda v: '['+str(v)+']', arr))))
