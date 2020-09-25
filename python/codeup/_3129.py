s = input()
o = 0
c = 0


def solution(s):
    global o, c
    for i in range(len(s)):
        if s[i] == "(":
            o += 1
        else:
            c += 1
        if o < c:
            return 'bad'
    if o == c:
        return 'good'
    return 'bad'


print(solution(s))
