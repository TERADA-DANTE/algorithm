from collections import deque
queue = deque(list(input()))
answer = 0
stack = []
while queue:
    bowel = queue.popleft()
    if not stack:
        stack.append(bowel)
        answer += 10
    else:
        if stack[-1] != bowel:
            answer += 10
        else:
            answer += 5
        stack.append(bowel)
print(answer)
