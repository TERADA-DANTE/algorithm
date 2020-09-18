string = list(input())
flag = False
answer = ''
while string:
    s = string.pop(0)
    if s == ':':
        flag = not flag
    if flag:
        answer += s
print(int(answer[1:]))
