from collections import deque
k = int(input())
paths = [list(map(int, input().split())) for _ in range(6)]


def solution(k, paths):
    horizontals = [d for o, d in paths if o == 1 or o == 2]
    verticals = [d for o, d in paths if o == 3 or o == 4]
    queue = deque(paths)
    W = max(horizontals)
    H = max(verticals)
    area = W*H
    while queue:
        o, d = queue.popleft()
        if d == W and o <= 2:
            queue.appendleft([o, d])
            break
        else:
            queue.append([o, d])
    if queue[0][0] == 1:
        # ㄴ j 1번 2번은 같음
        if queue[3][0] == 3:
            return area - queue[3][1]*queue[4][1]
        elif queue[3][0] == 4:
            return area - queue[2][1]*queue[3][1]
    elif queue[0][0] == 2:
        if queue[3][0] == 3:
            return area - queue[3][1]*queue[2][1]
        elif queue[3][0] == 4:
            return area - queue[4][1]*queue[3][1]

        # r ㄱ


print(k*solution(k, paths))
