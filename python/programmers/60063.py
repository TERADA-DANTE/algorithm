from collections import deque


def solution(board):
    length = len(board)
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    isVisited = {'0001': True}
    queue = deque([[[0, 0], [0, 1], 0]])

    def stringify(left, right):
        return ''.join(list(map(str, left))) + ''.join(list(map(str, right)))

    def isMovable(left, right):
        if isVisited.get(stringify(left, right)):
            return False
        for row, col in [left, right]:
            if not 0 <= row < length or not 0 <= col < length or board[row][col]:
                return False
        isVisited[stringify(left, right)] = True
        return True

    while queue:
        l, r, time = queue.popleft()
        if any([True if row == length-1 and col == length-1 else False for row, col in [l, r]]):
            return time
        l, r = sorted([l, r], key=lambda v: (v[0], v[1]))
        for move in moves:
            nexts = [list(map(sum, zip(l, move))),
                     list(map(sum, zip(r, move)))]
            if isMovable(*nexts):
                queue.append([*nexts, time+1])
        lr, lc = l
        rr, rc = r
        if lr == rr:
            if 0 <= lr-1 < length and 0 <= lc+1 < length and not board[lr-1][lc] and not board[lr-1][lc+1]:
                next = sorted([[lr-1, lc+1], r], key=lambda v: (v[0], v[1]))

                if not isVisited.get(stringify(*next)):
                    isVisited[stringify(*next)] = True
                    queue.append([*next, time+1])
            if 0 <= lr+1 < length and 0 <= lc+1 < length and not board[lr+1][lc] and not board[lr+1][lc+1]:
                next = sorted([[lr+1, lc+1], r], key=lambda v: (v[0], v[1]))

                if not isVisited.get(stringify(*next)):
                    isVisited[stringify(*next)] = True
                    queue.append([*next, time+1])
            if 0 <= rr-1 < length and 0 <= rc-1 < length and not board[rr-1][rc] and not board[rr-1][rc-1]:
                next = sorted([l, [rr-1, rc-1]], key=lambda v: (v[0], v[1]))

                if not isVisited.get(stringify(*next)):
                    isVisited[stringify(*next)] = True
                    queue.append([*next, time+1])
            if 0 <= rr+1 < length and 0 <= rc-1 < length and not board[rr+1][rc] and not board[rr+1][rc-1]:
                next = sorted([l, [rr+1, rc-1]], key=lambda v: (v[0], v[1]))

                if not isVisited.get(stringify(*next)):
                    isVisited[stringify(*next)] = True
                    queue.append([*next, time+1])
        else:
            if 0 <= lr+1 < length and 0 <= lc-1 < length and not board[lr][lc-1] and not board[lr+1][lc-1]:
                next = sorted([[lr+1, lc-1], r], key=lambda v: (v[0], v[1]))
                if not isVisited.get(stringify(*next)):
                    isVisited[stringify(*next)] = True
                    queue.append([*next, time+1])
            # 아래
            if 0 <= lr+1 < length and 0 <= lc+1 < length and not board[lr][lc+1] and not board[lr+1][lc+1]:
                next = sorted([[lr+1, lc+1], r], key=lambda v: (v[0], v[1]))
                if not isVisited.get(stringify(*next)):
                    isVisited[stringify(*next)] = True
                    queue.append([*next, time+1])
            # 오른쪽
            # 위
            if 0 <= rr-1 < length and 0 <= rc-1 < length and not board[rr][rc-1] and not board[rr-1][rc-1]:
                next = sorted([l, [rr-1, rc-1]], key=lambda v: (v[0], v[1]))
                if not isVisited.get(stringify(*next)):
                    isVisited[stringify(*next)] = True
                    queue.append([*next, time+1])
            # 아래
            if 0 <= rr-1 < length and 0 <= rc+1 < length and not board[rr][rc+1] and not board[rr-1][rc+1]:
                next = sorted([l, [rr-1, rc+1]], key=lambda v: (v[0], v[1]))

                if not isVisited.get(stringify(*next)):
                    isVisited[stringify(*next)] = True
                    queue.append([*next, time+1])
    return


print(solution(	[[0, 0, 0, 1, 1],
                 [0, 0, 0, 1, 0],
                 [0, 1, 0, 1, 1],
                 [1, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0]]))
