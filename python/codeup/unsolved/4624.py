from collections import deque
string = deque([s for s in input()])


def solution(queue):
    a, b, c, d = 0, 0, 0, 0
    stack = []
    # 괄호가 상쇄되면 숫자로 변경한다.
    while queue:
        q = queue.popleft()
        if q == '(':
            a += 1
        elif q == ')':
            b += 1
        elif q == '[':
            c += 1
        else:
            d += 1
        if b > a or d > c:
            return 0
        stack.append(q)
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                f = stack.pop()
                if f == '(':
                    stack.append(2)
                else:
                    stack.append(3)


print(solution(string))
