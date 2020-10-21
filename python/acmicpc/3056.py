from itertools import permutations
n = int(input())

agents = [list(map(int, input().split())) for _ in range(n)]

candidates = list(permutations(range(n), n))


def mul(tuples):
    result = 1
    for i in range(n):
        result *= float(agents[i][tuples[i]]/100)
    return result


def solution(agents, candidates):
    answer = 0
    for candidate in candidates:
        ret = mul(candidate)*100
        answer = max(answer, ret)
    return answer


print('%0.6f' % float(solution(agents, candidates)))
