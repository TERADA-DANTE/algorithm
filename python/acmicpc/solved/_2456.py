from collections import Counter
n = int(input())
votes = [list(map(int, input().split())) for _ in range(n)]


def solution(n, votes):
    candidates = [[0, []] for _ in range(3)]
    for a, b, c in votes:
        candidates[0][0] += a
        candidates[0][1].append(a)
        candidates[1][0] += b
        candidates[1][1].append(b)
        candidates[2][0] += c
        candidates[2][1].append(c)
    for i in range(3):
        candidates[i][1] = Counter(candidates[i][1])
        candidates[i] = [candidates[i][0], candidates[i][1]
                         [3], candidates[i][1][2], candidates[i][1][1], i+1]
    # 점수가 다 차이나는 경우
    answer = []
    for i in range(3):
        temp = 0
        for j in range(4):
            temp += candidates[i][j] * 10**(4-j)
        answer.append([temp, candidates[i][-1], candidates[i][0]])
    m = max([answer[i][0] for i in range(3)])
    tt = []
    for i in range(3):
        if answer[i][0] == m:
            tt.append(i)
    if len(tt) == 1:
        return [tt[0]+1, answer[tt[0]][-1]]
    else:
        return [0, answer[tt[0]][-1]]


print(*solution(n, votes))
