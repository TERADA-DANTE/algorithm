e, s, m = list(map(int, input().split()))


def solution(e, s, m):
    [E, S, M] = [0, 0, 0]
    l = 0
    # 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19
    while E != e or S != s or M != m:
        E += 1
        S += 1
        M += 1
        l += 1
        if E > 15:
            E = 1
        if S > 28:
            S = 1
        if M > 19:
            M = 1
    return l


print(solution(e, s, m))
