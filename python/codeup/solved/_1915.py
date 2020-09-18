def solution(n, answer=[1, 1]):
    if n < 3:
        return answer[n-1]
    return solution(n-1, [answer[1], sum(answer)])


print(solution(int(input())))
