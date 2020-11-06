def solution(a, b):
    x1, y1, x2, y2 = a
    i1, j1, i2, j2 = b
    # 다 안만나는 경우
    if x1 == i1:
        if y2 < j1:
            return 'd'
        elif y2 == j1:
            return 'b'
        elif y1 <= j1 < j2:
            return 'a'
        elif j1 < y1:
            if y1 < j2:
                return 'a'
            elif y1 == j2:
                return 'b'
            elif j2 < y1:
                return 'd'
    elif x1 < i1 < x2:
        if y2 < j1:
            return 'd'
        elif y2 == j1:
            return 'b'
        elif y1 <= j1 < y2:
            return 'a'
        elif j1 < y1:
            if y1 < j2:
                return 'a'
            elif y1 == j2:
                return 'b'
            elif j2 < y1:
                return 'd'
    elif x2 == i1:
        if y2 < j1:
            return 'd'
        elif y2 == j1:
            return 'c'
        elif y1 < j1 < y2:
            return 'b'
        elif j1 < y1:
            if y1 < j2:
                return 'b'
            elif y1 == j2:
                return 'c'
            elif j2 < y1:
                return 'd'
    elif x2 < i1:
        return 'd'


for _ in range(4):
    points = list(map(int, input().split()))
    a, b = [points[0:4], points[4:]]
    if b[0] < a[0]:
        a, b = b, a

    print(solution(a, b))
