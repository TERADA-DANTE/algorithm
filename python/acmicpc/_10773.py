stack = []
for _ in range(int(input())):

    n = int(input())
    if n:
        stack.append(n)
    elif not n and len(stack):
        stack.pop()
print(sum(stack))
