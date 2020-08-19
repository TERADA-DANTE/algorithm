s = input()


def solution(s):
    suffixes = [None] * len(s)
    for i in range(len(s)):
        suffixes[i] = s[i:]
    return '\n'.join(sorted(suffixes, key=lambda suffix: (suffix)))


print(solution(s))
