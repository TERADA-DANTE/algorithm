answer = []


def solution(clothes):
    cnt = 1
    for e in map(lambda v: len(v) + 1, clothes.values()):
        cnt *= e
    return cnt - 1


for _ in range(int(input())):
    clothes = dict()
    for _ in range(int(input())):
        value, key = input().split()
        if clothes.get(key):
            clothes[key].append(value)
        else:
            clothes[key] = [value]
    answer.append(solution(clothes))
print('\n'.join(list(map(str, answer))))
