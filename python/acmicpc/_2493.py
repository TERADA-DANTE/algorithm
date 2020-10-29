from collections import deque
n = int(input())

towers = list(map(int, input().split()))


def solution(n, towers):
    answers = [0] * (n+1)
    queue = deque()
    i = n
    while towers:
        index, tower = towers.pop()
        while queue:
            if tower > queue[-1][1]:
                idx, _ = queue.pop()
                answers[idx] = index
            else:
                break
        queue.append((index, tower))
        i -= 1
    while queue:
        idx, _ = queue.pop()
        answers[idx] = 0
    return answers[1:]


print(*solution(n, list(enumerate(towers, start=1))))
