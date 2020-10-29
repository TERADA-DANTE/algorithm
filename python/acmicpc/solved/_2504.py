import re
from collections import deque
brackets = deque(list(input()))


def solution(brackets):
    d = {
        '(': 0,
        ')': 0,
        '[': 0,
        ']': 0
    }
    chk = ''.join(brackets)
    while '()' in chk or '[]' in chk:
        chk = chk.replace('()', '')
        chk = chk.replace('[]', '')
    if chk != '':
        return 0
    stack = [brackets.popleft()]
    d[stack[0]] += 1
    while brackets:
        # print(stack)
        bracket = brackets.popleft()
        d[bracket] += 1
        if bracket == ')':
            i = len(stack)-1
            if stack[i] == '(':
                stack[i] = 2
            else:
                while i >= 0:
                    if stack[i] == '(':
                        stack.pop(i)
                        break
                    if isinstance(stack[i], int):
                        stack[i] *= 2
                    i -= 1
        elif bracket == ']':
            i = len(stack)-1
            if stack[i] == '[':
                stack[i] = 3
            else:
                while i >= 0:
                    if stack[i] == '[':
                        stack.pop(i)
                        break
                    if isinstance(stack[i], int):
                        stack[i] *= 3
                    i -= 1
        else:
            stack.append(bracket)
    return sum(stack)


print(solution(brackets))
