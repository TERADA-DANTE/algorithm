from collections import deque


def solution(number, k):
    queue = deque(list(number))
    stack = [queue.popleft()]
    while k and queue:
        q = queue.popleft()
        while k and stack and stack[-1] < q:
            stack.pop()
            k -= 1
        stack.append(q)
    return ''.join(stack[0:len(stack)-k]) if k else ''.join(stack + list(queue))


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
