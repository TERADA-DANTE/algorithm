from itertools import permutations
questions = int(input())
answers = [list(map(int, input().split())) for _ in range(questions)]
# 0:n, 1: m, 2:d, 3:t


def compare(candidate, target):
    strike, ball = 0, 0
    for i in range(3):
        if candidate[i] == target[i]:
            strike += 1
            continue
        if candidate[i] in target:
            ball += 1
    return strike, ball

    # 375
    # 576


def solution(answers):

    candidates = set([''.join(map(str, per))
                      for per in permutations([i for i in range(1, 10)], 3)])
    while answers:
        target, strike, ball = answers.pop()
        temp = set()
        for candidate in candidates:
            s, b = compare(str(candidate), str(target))
            if s == strike and b == ball:
                temp.add(candidate)
        candidates = candidates & temp
    return len(candidates)


print(solution(answers))
