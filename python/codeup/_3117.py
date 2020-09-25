n = int(input())
stack = []
for _ in range(n):
    i = int(input())
    if i:
        stack.append(i)
    elif not i and stack:
        stack.pop()
if stack:
    print(sum(stack))
else:
    print(0)
