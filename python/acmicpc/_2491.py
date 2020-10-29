from collections import deque
n = int(input())
numbers = list(map(int, input().split()))


def solution(n, numbers):
    # 증 한번하고 감한번하고
    answer = 0
    stack = [-1]
    increase = deque(numbers)
    while increase:
        number = increase.popleft()
        if number >= stack[-1]:
            stack.append(number)
        else:
            stack.clear()
            stack = [-1]
            stack.append(number)
        answer = max(answer, len(stack))

    stack = [10]
    decrease = deque(numbers)
    while decrease:
        number = decrease.popleft()
        if number <= stack[-1]:
            stack.append(number)
        else:
            stack.clear()
            stack = [10]
            stack.append(number)
        answer = max(answer, len(stack))
    return answer - 1


print(solution(n, numbers))
