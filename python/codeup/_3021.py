n = input()
m = input()
n, m = sorted([n, m], key=len)
n = n.rjust(len(m), '0')
answer = []
offset = 0
for i in range(len(m)-1, -1, -1):
    if int(n[i]) + int(m[i]) + int(offset) >= 10:
        answer.insert(0, (int(n[i]) + int(m[i]) + int(offset)) % 10)
        offset = 1
    else:
        answer.insert(0, (int(n[i]) + int(m[i]) + int(offset)) % 10)
        offset = 0
if offset:
    answer.insert(0, '1')
print(''.join(list(map(str, answer))))
