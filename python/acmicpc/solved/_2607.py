n = int(input())
initial = input()
candidates = [input() for _ in range(n-1)]


def isSame(initial, candidate):
    if set(initial) != set(candidate):
        return False
    for s in set(initial):
        if initial.count(s) != candidate.count(s):
            return False
    return True


def isSimmilar(initial, candidate):
    i = len(initial)
    c = len(candidate)
    # 같은 길이인경우
    if i == c:
        # 그대로 같은 문자인경우
        if isSame(initial, candidate):
            return 1
    # 하나 바꿔야 같은 문자인 경우
    # 카운트 같은건 일단 삭제?
        temp = list(candidate)
        for v in initial:
            if v in temp:
                temp.remove(v)
        if len(temp) == 1:
            return 1
        return 0
    # 같은 문자
    # 두개의 단어가 같은 종류의 문자로 이루어져 있다.
    # 같은 문자는 같은 개수 만큼 있다.
    # 이니셜이 한개 더 큰경우
    elif i == c+1:
        temp = list(initial)
        for v in candidate:
            if v in temp:
                temp.remove(v)
        if len(temp) == 1:
            return 1
        return 0
        # 이니셜이 한개 더 작은 경우
        # 이니셜에 한개 더 추가해서 같은 문자를 만들어야함
        # DOG
        # DLGO
    elif i+1 == c:
        temp = list(candidate)
        for v in initial:
            if v in temp:
                temp.remove(v)
        if len(temp) == 1:
            return 1
        return 0
    else:
        return 0


def solution(n, initial, candidates):
    answer = 0
    for i in range(1, n):
        candidate = candidates[i-1]
        answer += isSimmilar(initial, candidate)
        #print(candidate, answer)
    return answer


print(solution(n, initial, candidates))
