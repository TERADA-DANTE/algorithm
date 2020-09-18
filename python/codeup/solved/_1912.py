def solution(n, answer=1):
    if n:
        return solution(n-1, answer*n)
    return answer


print(solution(int(input())))
