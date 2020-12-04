from collections import deque

flag = True
string = deque(list(input()))
answer = ''
while string:
    s = string.popleft()
    if flag:
        answer += s
        flag = False
    if s == '-':
        flag = True
print(answer)
