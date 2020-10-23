import time
n = int(input())
coordinates = [list(map(lambda v: int(float(v)*10), input().split()))
               for _ in range(n)]


def solution(n, coordinates):
    d = dict()
    for x, y, width, height in coordinates:
        for i in range(height):
            for j in range(width):
                if not d.get(f'{x+i}.{y+j}'):
                    d[f'{x+i}.{y+j}'] = 1
    return sum(list(d.values()))


print(solution(n, coordinates))
