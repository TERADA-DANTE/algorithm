import math
Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = list(map(int, input().split()))


def gradient(x1, x2, y1, y2):
    [dx, dy] = list(map(abs, [x1-x2, y1-y2]))
    return dy/dx


def distance(x1, y1, x2, y2):
    return math.sqrt(sum(list(map(lambda v: abs(v)**2, [x1-x2, y1-y2]))))


left = [Ax, Ay, Cx, Cy]
right = [Bx, By, Dx, Dy]
mid =
if gradient(Ax, Bx, Ay, By) == gradient(Cx, Dx, Cy, Dy):
    print(distance(Ax, Cx, Ay, Cy))
else:
