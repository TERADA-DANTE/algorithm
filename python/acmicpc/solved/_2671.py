import re
s = input()


def solution(s):

    if re.fullmatch(r'(100+1+|01)+', s):
        return "SUBMARINE"
    return 'NOISE'


print(solution(s))
