n = int(input())
a = n
m = int(input())
b = m
n, m = sorted([n, m])
m = str(m)
n = str(n).rjust(len(m), '0')
answer = []
offset = 0
for i in range(len(m)-1, -1, -1):
    # m 이 큰수
    if int(m[i]) - int(n[i]) + offset >= 0:
        answer.insert(0, int(m[i]) - int(n[i])+offset)
        offset = 0
    else:
        answer.insert(0, (10+int(m[i]) - int(n[i])+offset) % 10)
        offset = -1
c = int(''.join(list(map(str, answer))))
if a < b:
    print(-c)
else:
    print(c)
