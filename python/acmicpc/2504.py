from collections import deque
brackets = deque(list(input()))


def solution(brackets):
    d = {
        '(': 0,
        ')': 0,
        '[': 0,
        ']': 0
    }

    def isValid():
        return d['('] >= d[')'] and d['['] >= d[']']

    stack = [brackets.popleft()]
    d[stack[0]] += 1
    while brackets:
        bracket = brackets.popleft()
        d[bracket] += 1
        # 유효한 입력인지 검사.
        # 각 각의 괄호가 각각ㅂ의 괄호를 초과하거나
        # 서로다른 영역ㅇ`ㅔ `침범한 11ㅇ우경우`1
        # 스택에 쌓으면서 생각
        print(d)
        if not isValid():
            return False
        # 유효하면
        # 스택에 쌓아서 숫자로 변환

        stack.append(bracket)
    return 0


print(solution(brackets))
