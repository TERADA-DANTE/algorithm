from itertools import permutations, combinations
l, c = list(map(int, input().split()))
answer = []


def separate(words):
    [consonants, vowels] = [[], []]
    for word in words:
        if word in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(word)
        else:
            consonants.append(word)
    return [sorted(consonants), sorted(vowels)]


def isEligible(word):
    v = 0
    c = 0
    for w in word:
        if w in ['a', 'e', 'i', 'o', 'u']:
            v += 1
        else:
            c += 1
        if v >= 1 and c >= 2:
            return True
    return False


def solution(l, c):
    words = input().split()
    answer = []
    for word in combinations(words, l):
        if isEligible(word):
            answer.append(''.join(sorted(word)))
    return '\n'.join(sorted(answer))


print(solution(l, c))
