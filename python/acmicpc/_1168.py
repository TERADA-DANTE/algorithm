from collections import deque
n, k = list(map(int, input().split()))


def solution(n, k):
    # 1 2 3 4 5 6 7
    dq = deque()
    answer = []
    for i in range(n):
        dq.append(i+1)
    while len(dq):
        dq.rotate(-k+1)
        answer.append(dq.popleft())
    return '<' + ', '.join(map(str, answer)) + '>'


print(solution(n, k))
