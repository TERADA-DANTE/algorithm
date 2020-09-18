def solution(n, history=[]):
    if n == 1:
        return '\n'.join(reversed(list(map(str, history + [n]))))
    elif n % 2:
        return solution(3*n+1, history + [n])
    else:
        return solution(int(n//2), history + [n])


print(solution(int(input())))
