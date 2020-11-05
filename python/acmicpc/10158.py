col, row = list(map(int, input().split()))

position = list(map(int, input().split()))

k = int(input())


def solution(row, col, position, k):
    r, c = row-position[1], position[0]
    flag = [-1, 1]

    def next(r, c, flag):
        R, C = r+flag[0], c+flag[1]
        if 0 <= R <= row and 0 <= C <= col:
            return [R, C, flag]
        else:
            if r == row and c == col:
                return [row-1, col-1, [-1, -1]]
            if r == row and c == 0:
                return [row-1, 1, [-1, 1]]
            if r == 0 and c == 0:
                return [1, 1, [1, 1]]
            if r == 0 and c == col:
                return [1, col-1, [1, -1]]
            if c == col:
                return [r+flag[0], c-1, [flag[0], -flag[1]]]
            if c == 0:
                return [r+flag[0], c+1, [flag[0], -flag[1]]]
            if r == row:
                return [r-1, c+flag[1], [-flag[0], flag[1]]]
            if r == 0:
                return [r+1, c+flag[1], [-flag[0], flag[1]]]
    d = dict()
    answer = []
    for _ in range(k):
        r, c, flag = next(r, c, flag)
        if d.get(f'{r}.{c}.{flag[0]}.{flag[1]}'):
            break
        d[f'{r}.{c}.{flag[0]}.{flag[1]}'] = True
        answer.append([r, c])
    r, c = answer[(k-1) % len(answer)]
    return [c, row-r]


print(*solution(row, col, position, k))
