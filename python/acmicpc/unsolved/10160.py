n, k = list(map(int, input().split()))
temp = []


def solution(n, k):
    for a in ['a', 'b', 'c']:
        for b in ['a', 'b', 'c']:
            for c in ['a', 'b', 'c']:
                for d in ['a', 'b', 'c']:
                    for e in ['a', 'b', 'c']:
                        for f in ['a', 'b', 'c']:
                            for g in ['a', 'b', 'c']:
                                for i in range(3):
                                    if (a+b+c+d+e+f+g)[i:i+5] == 'abcbc' or (a+b+c+d+e+f+g)[i:i+5] == 'ababc':
                                        temp.append(a+b+c+d+e+f+g)
    return temp, len(temp)


print(solution(n, k))
