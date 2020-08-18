n = int(input())


def solution(n):
    answer = []
    i = 2
    while n != 1:
        if not n % i:
            answer.append(i)
            n /= i
        else:
            i += 1
    return '\n'.join(map(str, answer))


print(solution(n))
