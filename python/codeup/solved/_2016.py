import re
n = int(input())
string = [s for s in input()]
cnt = 0
answer = []
while string:
    s = string.pop()
    if not cnt % 3 and cnt:
        answer.insert(0, ',')

    answer.insert(0, s)
    cnt += 1
print(''.join(answer))
