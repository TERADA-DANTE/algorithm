from collections import deque

answer = float('inf')


def solution(strs, t):

    def execute(t, cnt):
        global answer
        if not t:
            answer = min(answer, cnt)
        for str in strs:
            if str == t[0:len(str)]:
                execute(t[len(str):], cnt+1)
    execute(t, 0)
    return -1 if answer == float('inf') else answer


print(solution(	["app", "ap", "p", "l", "e", "ple", "pp"], "apple"))
