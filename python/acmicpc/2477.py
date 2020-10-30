from collections import deque
k = int(input())
paths = [list(map(int, input().split())) for _ in range(6)]


def solution(k, paths):
    queue = deque(paths)
    widths = sorted([[o, d] for o, d in paths if o <= 2], key=lambda v: v[1])
    heights = sorted([[o, d] for o, d in paths if o > 2], key=lambda v: v[1])

    W = widths[-1][1]
    H = heights[-1][1]

    while queue:
        o, d = queue.popleft()
        if d == W:
            break
        else:
            queue.append([o, d])
    if queue[0][0] == 3:
        if queue[2][0] == 3:
            return W*H - queue[1][1]*queue[2][1]
        elif queue[2][0] == 4:
            return W*H - queue[3][1]*queue[2][1]

    elif queue[0][0] == 4:
        if queue[2][0] == 3:
            return W*H - queue[1][1]*queue[2][1]
        elif queue[2][0] == 4:
            return W*H - queue[2][1]*queue[3][1]
        # ㄴ or j


print(k*solution(k, paths))
