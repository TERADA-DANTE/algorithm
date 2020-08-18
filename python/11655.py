s = input()


def solution(s):
    answer = [None] * len(s)
    for i in range(len(s)):
        if s[i].isalpha():
            answer[i] = chr(ord(s[i])+13 if ord(s[i])+13
                            <= (90 if s[i].isupper() else 122) else ord(s[i])-13)
        else:
            answer[i] = s[i]

    return ''.join(answer)


print(solution(s))
