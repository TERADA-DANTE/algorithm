n = int(input())
initial = input()
candidates = [input() for _ in range(n-1)]


def isSame(word, target):
    for i in range(len(word)):
        if word[i] != target[i]:
            word[i] = target[i]
            break
    if word == target:
        return 1
    return 0


def isSimmilar(word, target):
    print(target)
    # 같은 구성 => 같은 길이에 같은 셋
    if abs(len(word)-len(target)) > 1:
        return 0
    if abs(len(word)-len(target)) == 0:
        if isSame(word, target):
            return 1
        return 0
    if len(word) == len(target) + 1:
        for t in target:
            if t in word:
                word.remove(t)
        if len(word) == 1:
            return 1
        return 0
    if len(word) == len(target) - 1:
        for w in word:
            if w in target:
                target.remove(w)
        if len(target) == 1:
            return 1
        return 0
        # 한글자 차이 나는 경우

        # 같은 구성이거나,

        # target에 하나를 더하거나, 빼거나 바꿔서 같은 구성


def solution(n, initial, candidates):
    answer = 0
    for i in range(1, n):
        candidate = candidates[i-1]
        answer += isSimmilar(list(initial), list(candidate))
        print(answer)
    return answer


print(solution(n, initial, candidates))
