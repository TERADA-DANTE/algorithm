n, m = list(map(int, input().split()))

left = list(input())
right = list(input())
t = int(input())


class Line:
    def __init__(self, data, offset):
        l = len(data)
        self.arr = [None] * l
        for i in range(l):
            self.arr[i] = [data[i], i*2 +
                           offset] if offset else [data[-i-1], i*2]

    def jump(self, t, direction):
        return [[value, index + direction * t] for value, index in self.arr]


def solution():
    l = Line(left, 0)
    r = Line(right, 2*len(left)-1)
    result = l.jump(t, 1) + r.jump(t, -1)
    result.sort(key=lambda v: v[1])
    return ''.join([value for value, _ in result])


print(solution())
