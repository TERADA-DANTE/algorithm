n, m = list(map(int, input().split()))
l = min(n, m)
b = list(map(int, input().split()))
g = list(map(int, input().split()))
boys, girls = b, g if len(b) <= len(g) else g, b


def solution(boys, girls):
    d = dict()

    def matching(boys, girls):
        if len(boys) == 1:

            d[f'{boys[0]}:{}']

        elif len(girls) == 1:

        else:

    return min(matching(boys, girls))


print(solution(boys, girls))
