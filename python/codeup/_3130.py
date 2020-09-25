n = int(input())
cows = [int(input()) for _ in range(n)]
answer = [0] * n
stack = [cows[0]]
for i in range(1, n):
    if i:
        if stack[-1] > cows[i]:
            stack.append(cows[i])
            answer[i] = len(stack)-1
        else:
            while stack:
                if stack[-1] <= cows[i]:
                    stack.pop()
                else:
                    answer[i] = len(stack)
                    stack.append(cows[i])
                    break
            if not stack:
                answer[i] = 0
                stack.append(cows[i])
print(sum(answer))
