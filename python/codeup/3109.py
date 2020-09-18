n = int(input())

stack = []
d = dict()
for _ in range(n):
    code, number, name = input().split()
    if code == 'I':
        if not d.get(number):
            stack.append([number, name])
            d[number] = True
    if code == 'D':
        if d.get(number):
            d[number] = False
            for i in range(len(stack)):
                if stack[i][0] == number:
                    stack.pop(i)
                    break
stack.sort(key=lambda v: int(v[0]))

corrects = list(map(int, input().split()))
for i in corrects:
    print(*stack[i-1])
