n, m = list(map(int, input().split()))
l = min(n, m)
boys = list(map(int, input().split()))
girls = list(map(int, input().split()))


def solution(boys, girls):
    boys.sort()
    girls.sort()
    cnt = 0
    for i in range(l):
        cnt += abs(boys[i]-girls[i])
    return cnt


print(solution(boys, girls))
