from collections import deque
string = deque([s for s in input()])


def solution(queue):
    a, b, c, d = 0, 0, 0, 0
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


print(solution(string))
