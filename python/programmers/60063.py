from collections import deque


def solution(board):
    answer = float('inf')
    length = len(board)
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    isVisited = {'0001': 0}
    queue = deque([[[0, 0], [0, 1], 0]])

    def sort(arr):
        return sorted(arr, key=lambda v: (v[0], v[1]))

    def stringify(left, right):
        return ''.join(map(str, left+right))

    def isMovable(left, right):
        if isVisited.get(stringify(left, right)) is not None:
            return False
        for row, col in [left, right]:
            if not 0 <= row < length or not 0 <= col < length or board[row][col]:
                return False
        return True

    while queue:
        l, r, time = queue.popleft()
        l, r = sort([l, r])
        flag = l[0] == r[0]
        if r[0] == r[1] == length-1:
            answer = min(answer, time)
            continue
        for a, b in moves:
            nexts = [[x+a, y+b] for x, y in [l, r]]
            if isMovable(*nexts):
                nexts = sort(nexts)
                isVisited[stringify(*nexts)] = time+1
                queue.append([*nexts, time+1])
        for i in [-1, 1]:
            for j in [-1, 1]:
                if i-1:
                    if 0 <= r[0]+(j if flag else i) < length and 0 <= r[1]+(i if flag else j) < length and not board[r[0]+(j if flag else 0)][r[1] + (0 if flag else j)] and not board[r[0] + (j if flag else i)][r[1]+(i if flag else j)]:
                        next = sort([l, [r[0]+j, r[1]+i]]
                                    ) if flag else sort([l, [r[0]+i, r[1]+j]])
                        if not isVisited.get(stringify(*next)):
                            isVisited[stringify(*next)] = time+1
                            queue.append([*next, time+1])
                else:
                    if 0 <= l[0]+(j if flag else i) < length and 0 <= l[1]+(i if flag else j) < length and not board[l[0]+(j if flag else 0)][l[1] + (0 if flag else j)] and not board[l[0] + (j if flag else i)][l[1]+(i if flag else j)]:
                        next = sort([[l[0]+j, l[1]+i], r]
                                    ) if flag else sort([[l[0]+i, l[1]+j], r])
                        if not isVisited.get(stringify(*next)):
                            isVisited[stringify(*next)] = time+1
                            queue.append([*next, time+1])
    return answer


print(solution([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))
